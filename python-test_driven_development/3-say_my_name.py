#!/usr/bin/python3

"""
Contain th modul with function say_my_name
"""


def say_my_name(first_name, last_name=""):

    """
    function for print first and last name

    first_name: contain first name
    last_name: contain last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
