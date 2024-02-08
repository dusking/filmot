"""
This file is part of Filmot API wrapper.

Filmot API is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.
"""
import json
import time
import queue
import asyncio
import logging
import threading
from random import randint
from datetime import timedelta
from functools import partial

from .dicts import DotDict

logger = logging.getLogger(__name__)


class Asyncit:  # pylint: disable=too-many-instance-attributes
    """Create Asyncit client, for simple run of function using asuncio.

    :param pool_size: Max function concurrent invocations.
    :param rate_limit: List of dicts with: max_calls, period_sec
    :param max_retry: If value greater than 1, retry function run in case of exception
    :param save_output: If true, function returned valued are saved in a queue.
    :param save_as_json: If true and save_output is true, function returned valued will be saved as json values.
    :param iter_indication: If true, a log will be printed every `iter` invocations
    Here is a sample usage example:
    >>> from asyncit import Asyncit
    >>> asyncit = Asyncit(iter_indication=10)
    >>> for i in range(100):
    >>>     asyncit.run(time.sleep, 1)
    In the following example the finction run will be limited by both pool size and rate limit:
    No more than 100 calls in 5 sec.
    >>> asyncit = Asyncit(
    >>>     save_output=True,
    >>>     save_as_json=True,
    >>>     pool_size=100,
    >>>     rate_limit=[{"period_sec": 5, "max_calls": 100}],
    >>>     iter_indication=100,
    >>> )
    >>> for i in range(100):
    >>>     asyncit.run(foo_call_some_api, arg1, arg2)
    >>> asyncit.wait()
    >>> return asyncit.get_output()
    """

    def __init__(
        self, pool_size=0, rate_limit=None, max_retry=None, save_output=False, save_as_json=False, iter_indication=None
    ):
        """Init Asyncit."""
        rate_limit = rate_limit or []
        self.futures = []

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError as error:
            logger.warning(f"{error}. Creating new event loop")
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        self.loop = loop

        self.save_output = save_output
        self.save_as_json = save_as_json
        self.output_queue = queue.Queue()  # QueueEx() if self.save_output else None
        self.sem = threading.Semaphore(pool_size) if pool_size else None
        self.clock_time = time.perf_counter
        self.raise_on_limit = True
        self.rate_limit = []
        self.max_retry = max_retry or 1
        self.iter_indication = iter_indication
        self.iter_counter = 0
        for limit in rate_limit:
            limit = DotDict(limit)
            self.rate_limit.append(
                DotDict(
                    dict(
                        max_calls=limit.max_calls,
                        period_sec=limit.period_sec,
                        last_reset=self.clock_time(),
                        num_calls=0,
                        total_calls=0,
                    )
                )
            )
        self.lock = threading.RLock()
        self.total_counter = 0
        self.total_run_start = self.clock_time()

    def __period_remaining(self, last_reset, period_sec) -> float:
        """Return the period remaining for the current rate limit window."""
        elapsed = self.clock_time() - last_reset
        return period_sec - elapsed

    def reset_start_time(self):
        """Reset the start time.

        To be used in case there is some time between Asyncit instance creation and the actual call time.
        """
        self.total_run_start = self.clock_time()

    def total_run_time(self):
        """Get the elapsed time, in a human-readable format."""
        elapsed_time = self.clock_time() - self.total_run_start
        return str(timedelta(seconds=elapsed_time)).split(".", maxsplit=1)[0]

    def func_wrapper(self, func, *args, **kwargs):
        """Wrap for the function execution."""
        if self.sem:
            self.sem.acquire()

        if self.rate_limit:
            with self.lock:
                for limit in self.rate_limit:
                    period_remaining = self.__period_remaining(limit.last_reset, limit.period_sec)

                    # If the time window has elapsed then reset.
                    if period_remaining <= 0:
                        limit.num_calls = 0
                        limit.last_reset = self.clock_time()

                    limit.num_calls += 1
                    limit.total_calls += 1
                    if limit.num_calls > limit.max_calls:
                        logger.info(f"going to sleep for {period_remaining:.2f} {limit}")
                        time.sleep(period_remaining)

        value = None
        retry_counter = 0
        exception = None

        while retry_counter < self.max_retry:
            retry_counter += 1
            try:
                value = func(*args, **kwargs)
                if self.iter_indication:
                    self.iter_counter += 1
                    if self.iter_counter % self.iter_indication == 0:
                        logger.info(f"running iter {self.iter_counter}")
                save_value = bool(value is not None and self.save_output and self.output_queue is not None)
                if save_value:
                    if self.save_as_json:
                        value = json.dumps(value)
                    self.output_queue.put(value)
                break
            except asyncio.CancelledError:
                logger.info("worker cancelled")
                break
            except Exception as ex:
                exception = ex
                if retry_counter < self.max_retry:
                    sleep_time = randint(1, 6)
                    logger.error(f"ex: {type(ex)}")
                    logger.info(f"sleep before retry: {sleep_time} sec ({self.rate_limit})")
                    time.sleep(sleep_time)
        else:
            logger.error(
                f"!!! Error: function {func.__name__} failed with args: {args} and kwargs: {kwargs}. "
                f"Exception caught: {exception}"
            )
        if self.sem:
            self.sem.release()
        return value

    def run(self, func, *args, **kwargs):
        """Execute the given function in async way.

        :param func: The function to be invoked.
        :param args: Positional arguments for the function.
        :param kwargs: Keyword arguments for the function.
        """
        func = partial(self.func_wrapper, func, *args, **kwargs)

        # Run tasks in the default loop's executor
        self.futures.append(self.loop.run_in_executor(None, func))

    def wait(self):
        """Wait for all run to be completed."""
        self.loop.run_until_complete(self._gather_with_concurrency())
        self.futures = []

    def get_output(self):
        """Get the returned values.

        >>> from asyncit import Asyncit
        >>> asyncit = Asyncit(
        >>>     save_output=True,
        >>>     save_as_json=True,
        >>>     pool_size=200,
        >>>     rate_limit=[{"period_sec": 5, "max_calls": 100}],
        >>>     iter_indication=100
        >>> )
        >>> for i in range(200):
        >>>     asyncit.run(echo, "A")
        >>> asyncit.wait()
        >>> return asyncit.get_output()
        """
        if not self.output_queue:
            return None

        items = []
        while not self.output_queue.empty():
            items.append(self.output_queue.get())

        if items and self.save_as_json:
            items = [json.loads(i) for i in items]  # pylint: disable=not-an-iterable

        return items

    async def _gather_with_concurrency(self):
        await asyncio.gather(*self.futures, return_exceptions=True)
