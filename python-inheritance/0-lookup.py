#!/usr/bin/python3

"""
Create a  function that returns the list of available attributes
"""


def lookup(obj):
    """
    return a function that returns the list
    of available attributes and methods of an object
    """

    return dir(obj)
