#!/usr/bin/python3
"""Module: that defines a student """


class Student:
    """ Class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves Class dictionary """
        return self.__dict__
