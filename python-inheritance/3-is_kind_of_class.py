#!/usr/bin/python3

"""
Create a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is exactly an instance
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance or if object is an instance of
        a_class
        False if obj is not an instance or if object is not an instance 
        of a_class
    """
    if isinstance(obj, a_class):
        return False
    else:
        return True
