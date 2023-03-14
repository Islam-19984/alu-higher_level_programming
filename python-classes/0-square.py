#!/usr/bin/python3

class Square:
    """Represents a square."""

    def __init__(self, side_length):
        """Initialize the square with the given side length."""
        self.side_length = side_length

    def area(self):
        """Return the area of the square."""
        return self.side_length ** 2

    def perimeter(self):
        """Return the perimeter of the square."""
        return 4 * self.side_length
