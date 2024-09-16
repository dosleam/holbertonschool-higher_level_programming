#!/usr/bin/python3

"""
Creates a class Square
"""


class Square:

    """
    defines a class Square

    Args:
        size (int): the size of the new square
        position (tuple): the postion of the square

    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self._position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Return the current square area
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
