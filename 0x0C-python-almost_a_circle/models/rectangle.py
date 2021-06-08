#!/usr/bin/python3
""" Module: rectangle.py """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ whidth the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format('width'))
        if value <= 0:
            raise ValueError("{} must be > 0".format('width'))
        self.__width = value

    @property
    def height(self):
        """ height the rectangle  """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format('height'))
        if value <= 0:
            raise ValueError("{} must be > 0".format('height'))
        self.__width = value

    @property
    def x(self):
        """ position in the `x` axis of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format('x'))
        if value < 0:
            raise ValueError("{} must be > 0".format('x'))
        self.__x = value

    @property
    def y(self):
        """ position in the `y` axis of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format('y'))
        if value < 0:
            raise ValueError("{} must be > 0".format('y'))
        self.__y = value

    def area(self):
        """ Area the rectangle """
        return (self.width * self.height)

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        print('\n' * self.x, end='')
        for i in range(self.height):
            print(' ' * self.y, end='')
            print('#' * self.width)

    def __str__(self):
        stdout = '[Rectangle] ({}) {}/{} - {}/{}'
        return stdout.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """  """
        list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list[arg], args[arg])

        for i in kwargs.keys():
            if i in dir(self):
                setattr(self, i, kwargs[i])
