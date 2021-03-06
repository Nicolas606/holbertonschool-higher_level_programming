#!/usr/bin/python3
"""Module: For defining the Square class.."""


class Square:
    """ Class Constructor"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, (int)) == 1:
            if size < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise ValueError("size must be an integer")
        if isinstance(position, str) == 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position, tuple) == 0 or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[0], str) == 1 or isinstance(
                        position[1], str) == 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(' '*self.__position[0], '#'*self.__size))

    @property
    def position(self):
        """ Private Attribute position Getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ Private Attribute position Setter """
        if isinstance(value, tuple) == 0 or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) == 0 or isinstance(value[1], int) == 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
