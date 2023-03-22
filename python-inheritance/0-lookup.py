#!/usr/bin/python3
"""list of available attributes and method of an object"""


def lookup(obj):
    """Return attributes
    Arg:
        - obj: objecg to get attributes
    """

    return dir(obj)
