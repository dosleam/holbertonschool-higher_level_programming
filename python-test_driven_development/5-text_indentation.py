#!/usr/bin/python3

"""
contain the function
"""


def text_indentation(text):

    """
    function for add indentation
    text: contain the string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    spec = {".", "?", ":"}
    start = 0
    for i in range(len(text)):
        if text[i] in spec:
            new_text = text[start:i + 1] + "\n\n"
            start = i + 1
            stripped = new_text.strip(" ")
            print("{}".format(stripped), end="")
    if start < len(text):
        result = text[start:].strip()
        print("{}".format(result), end="")
