"""
This file is part of Filmot API wrapper.

Filmot API is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.
"""
str_base = str, bytes, bytearray
items = "items"

_RaiseKeyError = object()  # singleton for no-default behavior


class DotDictMeta(type):
    """Metaclass for DotDict."""

    def __repr__(cls):
        """Return the name of the class."""
        return cls.__name__


class DotDict(dict, metaclass=DotDictMeta):
    """Dictionary that supports dot notation as well as dictionary access notation.

    Use the dot notation only for get values, not for setting.
    The Indexing operator (__getitem__) is not overriding to protect against bug
    relatedd to setting using d["a"] = {"key": "value"}

     usage:
     >>> d1 = DotDict()
     >>> d['val2'] = 'second'
     >>> print(d.val2)
    """

    __slots__ = ()
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, k):
        """Get property."""
        value = self.get(k)
        if isinstance(value, dict):
            return DotDict(value)
        return value

    def get(self, k, default=None):
        """Get value, returns default if key doesn't exist."""
        value = super().get(k, default)
        if isinstance(value, dict):
            return DotDict(value)
        return value

    def update(self, *args, **kwargs):
        """Update dictionary with key-value pairs."""
        super().update(*args, **kwargs)
        return self

    def copy(self):  # don't delegate w/ super - dict.copy() -> dict :(
        """Return a shallow copy of the dictionary."""
        return type(self)(self)
