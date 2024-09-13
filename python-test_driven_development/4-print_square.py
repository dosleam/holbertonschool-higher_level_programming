#!/usr/bin/python3

"""Create function print square"""


def print_square(size):

    """Print a square with the # character

    Args:
        size (int): size of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for cpt in range(size):
        [print("#", end="") for cpt2 in range(size)]
        print("")
