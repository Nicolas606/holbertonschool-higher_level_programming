#!/usr/bin/python3
"""Module: For defining the Rectangle class.."""


class Rectangle:
    """ Class: For defining a Rectangule object. """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Private Attribute width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private Attribute width Setter """
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Private Attribute height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private Attribute height Setter """
        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        raise TypeError("height must be an integer")
