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


class SearchResponse(BaseResponse):
    """Response class for search results."""

    def __init__(self, query: str, result: dict, hits: list, subtitles: list, more_results: list):
        """
        Initialize a SearchResponse object.

        Args:
            query (str): The search query string.
            result (dict): The search result.
            hits (list): List of hit items - inside the the result subtitles.
            subtitles (list): The first result subtitles, as list of lines data.
            more_results (list): Next video_id that match the query.
        """
        self.query = query
        self.result = DotDict(result)
        self.hits = sorted([DotDict(hit) for hit in hits], key=lambda x: float(x["start"]))
        self.subtitles = [DotDict(subtitle) for subtitle in subtitles]
        self.more_results = more_results[1:]  # skip first result as it already in the result property
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
        return f"{self.query}-{self.result.id}"

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
        first_hit = self.hits[index]
        hit_line = 0
        for i, line in enumerate(self.subtitles[1:]):
            if float(line.s) > float(first_hit.start):
                hit_line = i
                break
        hit_start_line = hit_line - 1
        hit_end_line = hit_line + 2
        text = " ".join([item.txt for item in self.subtitles[hit_start_line:hit_end_line]])
        start = self.subtitles[hit_line - 1].s
        response = {
            "link": f"https://www.youtube.com/watch?v={self.result.id}&t={start}s",
            "text": text,
        }
        return response

    def hits_data(self) -> list:
        """
        Get the 'index' hit data in the subtitles.

        Returns:
            dict: Dictionary containing hit data.
        """
        result = []
        hit_line = 0
        search_from = 1
        for hit in self.hits:
            for i, line in enumerate(self.subtitles[search_from:]):
                if float(line.s) > float(hit.start):
                    hit_line = i + search_from
                    break
            search_from = hit_line + 1
            hit_start_line = hit_line - 2
            hit_end_line = hit_line + 2
            text = " ".join([item.txt for item in self.subtitles[hit_start_line:hit_end_line]])
            start = self.subtitles[hit_start_line].s
            result.append(
                {
                    "link": f"https://www.youtube.com/watch?v={self.result.id}&t={start}s",
                    "text": text,
                }
            )
        return result
