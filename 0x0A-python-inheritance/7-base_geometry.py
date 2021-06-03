#!/usr/bin/python3
""" Module: inherits_from"""


class BaseGeometry():
    """ class BaseGeometry """

    def area(self):
        """ method no implement """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ method validator the value argument """
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
