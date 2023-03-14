#!/usr/bin/python3

class Square:
    """Represents a square."""

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        print(self)
        return 4 * self.side_length
