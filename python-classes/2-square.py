#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """creates a square.
    Private instance attributes: size
    """

    def __init__(self, size=0):
        """Initializes data."""
        if not isinstance(size, int):
            raise TypError("size must be an integer")
        elif size < 0:
            raise VaueError("size must be >= 0")
        self.__size = size
