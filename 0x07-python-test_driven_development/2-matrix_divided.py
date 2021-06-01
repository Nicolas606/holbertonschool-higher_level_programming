#!/usr/bin/python3
"""Module: matrix_divided"""


def matrix_divided(matrix, div):
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []

    if type(matrix) != list or len(matrix) is 0:
        raise TypeError(error_msg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) != list:
            raise TypeError(error_msg)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_content = []
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(error_msg)
            new_content.append(round(j/div, 2))
        new_matrix.append(new_content)
    return new_matrix
