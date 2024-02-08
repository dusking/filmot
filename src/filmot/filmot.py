"""
This file is part of Filmot API wrapper.

Filmot API wrapper is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.

This is the main module for the Filmot API wrapper.
It contains wrpper functoins for the Filmot REST API.
"""
import logging
import requests

from typing import Literal, Union, Optional

from .config import Config
from .asyncit import Asyncit
from .consts import Categories, Countries, Language
from .responses import SearchResponse
from .exceptions import FilmotException

logger = logging.getLogger(__name__)

VALID_CATEGORIES = Categories.get_all_categories()
VALID_COUNTRIES = Countries.get_all_codes()
VALID_LANGUAGES = Language.get_all_codes()


class Filmot:
    """Filmot API Wrapper."""

    def __init__(self, rapidapi_key: Optional[str] = None):
        """
        Initialize a Filmot Client object.

        Args:
            rapidapi_key (str, optional): The RapidAPI key. If None, the value will be taken from the config file.
        """
        self._config = Config()
        self.rapidapi_key = rapidapi_key or self._config.rapidapi_key
        self.rapidapi_host = self._config.rapidapi_host
        self.base_url = f"https://{self.rapidapi_host}"

    @staticmethod
    def set_rapidapi_key(value):
        """
        Set the RapidAPI key in the config file.

        Args:
            value (str): The RapidAPI key value.
        """
        config = Config()
        config.rapidapi_key = value
        config.rapidapi_host = "filmot-tube-metadata-archive.p.rapidapi.com"
        if config.save():
            print("Credentials set successfully!")

    def send_api(self, cmd: str, query: dict) -> dict:
        """
        Send the API request.

        rgs:
            cmd: The command to send.
            query: The query data.
        """
        headers = {
            "X-RapidAPI-Key": self.rapidapi_key,
            "X-RapidAPI-Host": self.rapidapi_host,
        }
        try:
            url = f"{self.base_url}/{cmd}"
            response = requests.get(url, headers=headers, params=query)
            if response.status_code >= 400:
                logger.error(f"API `{cmd}` failed with {response.status_code}: {response.content.decode('utf-8')}")
            response.raise_for_status()
            json_response = response.json()
            return json_response
        except requests.exceptions.HTTPError as http_err:
            raise FilmotException(f"Failed with HTTP {http_err}: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise FilmotException(f"Failed to send request: {req_err}")
        except ValueError as ex:
            raise FilmotException(f"Failed to parse JSON response: {ex}")

    def search_one(self, query_params: dict) -> SearchResponse:
        """
        Perform a single search.

        Args:
            query_params (dict): Parameters for the search.

        Returns:
            SearchResponse: The response for the search.
        """
        logger.info(f"Searching for {query_params}")
        return SearchResponse(query=query_params["query"], **self.send_api("getsubtitlesearch", query_params))

    def search(
        self,
        query: str,
        language: Optional[str] = None,
        category: Optional[str] = None,
        exclude_category: Optional[str] = None,
        license: Optional[Union[int, Literal[1, 2]]] = None,
        max_views: Optional[int] = None,
        min_views: Optional[int] = None,
        min_likes: Optional[int] = None,
        country: Optional[int] = None,
        channel_id: Optional[str] = None,
        title: Optional[str] = None,
        start_duration: Optional[int] = None,
        end_duration: Optional[int] = None,
        search_manual_subs: Optional[Union[int, Literal[1, 2]]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 10,
    ):
        """
        Perform a search equest.

        Args:
            query (str, required): The search query. the text which is being found in the subtitle data.
            language (str, optional): A two letter code that can be used to limit the search to only work on
                subtitles with the specified language.
            category (str, optional): Exact string for the video category.
            exclude_category (str, optional): A comma delimited list of categories to be excluded from the results.
                For example Music,Gaming
            license (Union[int, Literal[1, 2]], optional): The license type of the video:
                1 for standard YouTube License
                2 for creative Commons License
            max_views (int, optional): The maximum number of views. Defaults to None.
            min_views (int, optional): The minimum number of views. Defaults to None.
            min_likes (int, optional): The minimum number of likes. Defaults to None.
            country (int, optional): Numeric code representing the country to filter,
                this is the country as specified by the channel owner, could be unreliable.
            channel_id (str, optional): Limit the search to this specific channel id.
            title (str, optional): Query to filter by the title of the video.
            start_duration (int, optional): Minimal duration of the video in seconds.
            end_duration (int, optional): Maximal duration of the video in seconds.
            search_manual_subs (Union[int, Literal[1, 2]], optional): Whether to search manual subs.
                Set to 1 to search in manual subtitles, default searches in automatic subtitles
            start_date (str, optional): The start date. Defaults to None.
            end_date (str, optional): The end date. Defaults to None.
            limit (int, optional): The limit videos to return. Defaults to 10.

        Returns:
            list: List of SearchResponse objects.
        """

        def add_param(name, value):
            # Helper function to add a parameter to the query_params list
            if value is not None:
                if name == "category":
                    assert value in VALID_CATEGORIES
                if name == "country":
                    assert value in VALID_COUNTRIES
                if name == "language":
                    assert value in VALID_LANGUAGES
                query_params[name] = value

        query_params = {}
        add_param("query", f'"{query}"' if " " in query else query)
        add_param("lang", language)
        add_param("category", category)
        add_param("excludeCategory", exclude_category)
        add_param("license", license)
        add_param("maxViews", max_views)
        add_param("minViews", min_views)
        add_param("minLikes", min_likes)
        add_param("country", country)
        add_param("channelID", channel_id)
        add_param("title", title)
        add_param("startDuration", start_duration)
        add_param("endDuration", end_duration)
        add_param("searchManualSubs", search_manual_subs)
        add_param("startDate", start_date)
        add_param("endDate", end_date)

        response = self.search_one(query_params)
        result = [response]

        more_results = [i["id"] for i in response.more_results[: limit - 1]]

        asyncit = Asyncit(save_output=True)
        for video_id in more_results:
            temp_query_params = query_params.copy()
            temp_query_params["queryVideoID"] = video_id
            asyncit.run(self.search_one, temp_query_params)
        asyncit.wait()
        responses = asyncit.get_output()
        result.extend(responses)

        return result
