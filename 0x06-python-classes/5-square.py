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

    def area(self):
        """ method that returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """ Private Attribute size Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Private Attribute size Setter """
        if isinstance(value, (int)) == 1:
            if value < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise ValueError("size must be an integer")

    def my_print(self):
        """ Method that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size - 1):
                for j in range(self.__size):
                    print("#", end="")
                print()
