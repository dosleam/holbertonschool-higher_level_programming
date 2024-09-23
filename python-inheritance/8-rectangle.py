#!/usr/bin/python3

"""
Contain the class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Contain the code
    """

    def __init__(self, width, height):
        """
        Initialize the new Rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
