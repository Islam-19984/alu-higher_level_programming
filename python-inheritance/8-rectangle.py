#!/usr/bin/python3
"""Inherits BaseGeometry class documented now"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def _init_(self, width, height):
        """Initialize data."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
