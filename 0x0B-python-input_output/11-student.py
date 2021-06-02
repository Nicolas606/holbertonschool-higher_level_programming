#!/usr/bin/python3
"""Module: that defines a student """


class Student:
    """ Class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves Class dictionary """
        if attrs is None:
            return self.__dict__

        directory = {}
        if isinstance(attrs, list):
            for i in attrs:
                if i in self.__dict__:
                    directory[i] = self.__dict__[i]
        return directory

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance """
        for key in json.keys():
            self.__dict__[key] = json[key]
