#!/usr/bin/python3

"""
Creates a class Square
"""


class Square:

    """
    defines a class Square

    Args:
        size (int): the size of the new square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
