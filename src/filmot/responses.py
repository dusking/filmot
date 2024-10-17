"""
This file is part of Filmot API wrapper.

Filmot API is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.
"""
import logging

from .responses_base import BaseResponse
from .dicts import DotDict

logger = logging.getLogger(__name__)


class VideoInfo(BaseResponse):
    """VideoInfo class for video info in search results."""

    def __init__(self, **kwargs):
        """Initialize a VideoInfo object."""
        self.id = kwargs.get("id")
        self.title = kwargs.get("title")
        self.duration = kwargs.get("duration")
        self.upload_date = kwargs.get("uploaddate")
        self.view_count = kwargs.get("viewcount")
        self.like_count = kwargs.get("likecount")
        self.channel_id = kwargs.get("channelid")
        self.language = kwargs.get("lang")
        self.category = kwargs.get("category")
        self.channel_name = kwargs.get("channelname")
        self.channel_sub_count = kwargs.get("channelsubcount")
        self.channel_country_name = kwargs.get("channelcountryname")
        self.channel_thumbnail_url = kwargs.get("channelthumbnailurl")
        super().__init__()

    class Meta:
        """Meta class for VideoInfo."""

        main_field = "id"


class SearchResponse(BaseResponse):
    """Response class for search results."""

    def __init__(self, query: str, result: dict):
        """
        Initialize a SearchResponse object.

        Args:
            query (str): The search query string.
            result (dict): The search result.
            hits (list): List of hit items - inside the the result subtitles.
            subtitles (list): The first result subtitles, as list of lines data.
            more_results (list): Next video_id that match the query.
        """
        hits = result["hits"]
        category = result["category"]
        self.query = query
        self.category = category
        self.video_info = VideoInfo(**result)
        self.hits = sorted([DotDict(hit) for hit in hits], key=lambda x: float(x["start"]))
        # self.subtitles = [DotDict(subtitle) for subtitle in subtitles]
        # self.more_results = more_results[1:]  # skip first result as it already in the result property
        super().__init__()

    class Meta:
        """Meta class for SearchResponse."""

        main_field = "main_field"

    @property
    def main_field(self) -> str:
        """
        Get the main field.

        Returns:
            str: The main field.
        """
        return f"{self.query} {self.video_info.id}"

    def hit_count(self) -> int:
        """Get amount of hits."""
        return len(self.hits)

    def hit_data(self, index: int = 0) -> dict:
        """
        Get the 'index' hit data in the subtitles.

        Args:
            index (int): The index of the hit data. Defaults to 0.

        Returns:
            dict: Dictionary containing hit data.
        """
        hit = self.hits[index]
        text = hit.ctx_before + self.query + hit.ctx_after
        response = {
            "link": f"https://www.youtube.com/watch?v={self.video_info.id}&t={hit.start}s",
            "text": text,
        }

        # first_hit = self.hits[index]
        # hit_line = 0
        # for i, line in enumerate(self.subtitles[1:]):
        #     if float(line.s) > float(first_hit.start):
        #         hit_line = i
        #         break
        # hit_start_line = hit_line - 1
        # hit_end_line = hit_line + 2
        # text = " ".join([item.txt for item in self.subtitles[hit_start_line:hit_end_line]])
        # start = self.subtitles[hit_line - 1].s
        # response = {
        #     "link": f"https://www.youtube.com/watch?v={self.video_info.id}&t={start}s",
        #     "text": text,
        # }
        return response

    def hits_data(self) -> list:
        """
        Get the 'index' hit data in the subtitles.

        Returns:
            dict: Dictionary containing hit data.

        The goal is to create a list of hits, and for each hit to prepend previous line and append next line,
        so the provided text will have more context.
        """
        result = []
        # hit_line = 0
        # search_from = 1
        for hit in self.hits:
            try:
                text = hit.ctx_before + f" {self.query} " + hit.ctx_after
                result.append(
                    {
                        "link": f"https://www.youtube.com/watch?v={self.video_info.id}&t={hit.start}s",
                        "text": text,
                    }
                )

                # for i, line in enumerate(self.subtitles[search_from:]):
                #     if float(line.s) > float(hit.start):
                #         hit_line = i + search_from
                #         break
                # search_from = hit_line + 1  # next time search from next line
                # hit_start_line = hit_line - 2  # prepend previous 2 lines
                # hit_end_line = hit_line + 2  # append next 2 lines
                # text = " ".join([item.txt for item in self.subtitles[hit_start_line:hit_end_line] if item and item.txt])
                # start = self.subtitles[hit_start_line].s
                # result.append(
                #     {
                #         "link": f"https://www.youtube.com/watch?v={self.video_info.id}&t={start}s",
                #         "text": text,
                #     }
                # )
            except Exception as ex:
                logger.warning(f"Failed to get hits_data: {ex}")
                break
        return result
