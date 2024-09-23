#!usr/bin/python3

"""Create a function that returns True
if the object is exactly an instance of the specified class
otherwise False"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance
    
    Args:
        obj: object
        a_class: class
    Returns:
        True if object is exactly an instance of a a_class
        False if object is not an instance of a a_class
    """
    if type(obj) is not a_class:
        return False
    return True
