#!/usr/bin/python3
"""Module: For defining the Square class.."""


class Square:

    def __init__(self, size=0):
        """ Class Constructor"""
        if isinstance(size, (int)) == 1:
            if size < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise ValueError("size must be an integer")

    def area(self):
        """ method that returns the current square area"""
        return self.__size ** 2
