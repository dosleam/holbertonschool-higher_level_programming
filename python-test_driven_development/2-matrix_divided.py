#!/usr/bin/python3

"""Contain the matrix_divided fonction"""


def matrix_divided(matrix, div):

    """
    matrix_divided Divide each number by div

    matrix: contain the matrice
    div: contain the divisor
    """

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
