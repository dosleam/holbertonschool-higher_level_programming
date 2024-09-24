#!/usr/bin/python3

"""
Contain the class
"""


from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """
    Contain the method
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Contain the circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius * self.radius)

    def perimeter(self):
        return abs((2 * self.radius) * pi)


class Rectangle(Shape):
    """
    Contain the rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Contain the test method
    """

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
