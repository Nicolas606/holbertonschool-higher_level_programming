#!/usr/bin/python3
""" Module: inherits_from"""


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class rectangle that inherist of the class BaseGeometry  """

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
