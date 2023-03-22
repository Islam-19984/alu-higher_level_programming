#!/usr/bin/python3
"""Checks objec class"""


def is_same_class(obj, a_class):
    """Check object to class
    Args:
        - obj: object to class
        - a_class: class to check
    """
    return type(obj) is a_class
