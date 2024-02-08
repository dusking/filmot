"""
This file is part of Filmot API wrapper.

Filmot API is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by the Massachusetts
Institute of Technology.

For full details, please see the LICENSE file located in the root
directory of this project.
"""


class FilmotException(Exception):
    """Custom exception class for the Filmot wrapper."""

    def __init__(self, message: str):
        """
        Initialize the custom exception.

        :param message: exception message.
        """
        self.message = message
