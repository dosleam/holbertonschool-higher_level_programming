#!/usr/bin/python

"""
Contain the class
"""


class SwimMixin:
    """
    Contain the swimmixing class
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Contain the flyMixin class
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Contain the dragon class
    """

    def roar(self):
        print("The dragon roars!")
