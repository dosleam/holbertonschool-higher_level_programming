#!/usr/bin/python3

"""
Contain the class
"""


def inherits_from(obj, a_class):
    """
    Contain the code
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
