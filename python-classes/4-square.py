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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current square area
        """
        return self.__size ** 2
