#!/usr/bin/python3
"""Module: For defining the Rectangle class.."""


class Rectangle:
    """ Class: For defining a Rectangule object. """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Method that initializes the class """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        else:
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
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Method that returns the rectangle area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Method that print the rectangle with the character # """
        str_rect = ''
        if self.__width == 0 or self.__height == 0:
            return str_rect
        else:
            symbol = str(self.print_symbol)
            for i in range(self.__height):
                str_rect += "{}".format(symbol * self.__width)
                if i != (self.__height - 1):
                    str_rect += '\n'
        return str_rect

    def __repr__(self):
        """ Method that returns Object Representation as string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """This method Action when object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """staticmethod that returns the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ classcmethod that returns a new Rectangle"""
        return cls(size, size)
