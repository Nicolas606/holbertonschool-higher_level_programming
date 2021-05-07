#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = matrix.copy()
    i = 0
    while i < len(matrix):
        copy[i] = list(map(lambda x: x ** 2, matrix[i]))
        i += 1
    return copy
