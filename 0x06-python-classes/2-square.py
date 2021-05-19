#!/usr/bin/python3
"""Module: For defining the Square class.."""


class Square:
    """ Class Constructor"""
    def __init__(self, size=0):
        if isinstance(size, (int)) == 1:
            if size < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise ValueError("size must be an integer")
