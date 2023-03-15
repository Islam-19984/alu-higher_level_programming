#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size(int): The size of the new square."""

            if not isinstance(size, int):
                raise TypError("size must be an integer")
                elif size < 0:
                    raise VaueError("size must be >= 0")
                self.__size = size
