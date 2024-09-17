#!/usr/bin/python3

"""
Rectangle class
"""


class Rectangle:

    """
    arguments and methods
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        lines = []
        for line in range(self.height):
            rectangle += str(self.print_symbol) * self.width
            if line != (self.height - 1):
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
