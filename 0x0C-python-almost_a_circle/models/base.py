#!/usr/bin/python3
"""  """


class Base:
    """ This class will be the “base” of all other classes in this project."""
    __nb_objects = 0
    def __init__(self, id=None):
        self.__id = id
