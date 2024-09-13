#!/usr/bin/python3

"""Create function print square"""


def text_indentation(text):

    """Prints text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text (str): The string to print
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    for cpt in text:
        string += cpt
        if cpt in ['.', '?', ':']:
            string += "\n\n"
    print(string, end="")
