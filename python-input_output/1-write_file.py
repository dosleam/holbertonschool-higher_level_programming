#!/usr/bin/python3

"""
Define function
"""


def write_file(filename="", text=""):
    """
    Read files
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
