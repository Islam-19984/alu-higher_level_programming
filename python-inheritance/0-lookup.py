#!/usr/bin/python3


def lookup(obj):
    """
    Return a list of available attributes and mothods of an object.
    """
    attrs = dir(obj)
    methods = [attr for attr in atrs if callable(getatter(obj, attr))]
    return atrrs + methods
