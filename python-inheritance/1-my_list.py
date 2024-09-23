#!/usr/bin/python3

"""
Create a class Mylist that inherits from list
"""

class MyList(list):
    """My list that inherits from list"""

    def print_sorted(self):
        """return a list sorted"""
        print(sorted(self))
