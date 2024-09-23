#!/usr/bin/python3

"""
Contain the class
"""


def inherits_from(obj, a_class):

    """
    Contain the code
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
