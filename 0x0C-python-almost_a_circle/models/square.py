#!/usr/bin/python3
""" Module: rectangle.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class  Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    @property
    def size(self):
        """ Size square """
        return self.width

    @size.setter
    def size(self , value):
        self.width = value
        self.height = value

    def __str__(self):
        stdout = '[Square] ({}) {}/{} - {}'
        return stdout.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update  """
        list = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list[arg], args[arg])

        for i in kwargs.keys():
            if i in dir(self):
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """ Dictionary """
        dictionary = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dictionary
