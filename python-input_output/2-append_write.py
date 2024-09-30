#!/usr/bin/python3

"""
Read file
"""


def append_write(filename="", text=""):
    """
    Append a string

    Args:
        filename: name of file
        Text: text to append
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
