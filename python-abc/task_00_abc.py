#!/usr/bin/python3

"""
Contain the class
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Contain the parent class
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Contain the dog sound
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Contain the cat sound
    """

    def sound(self):
        return "Meow"
