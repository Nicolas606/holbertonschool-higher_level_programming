#!/usr/bin/python3
"""Module: print_square"""


def print_square(size):
    """ function that prints a square with the character # """
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
