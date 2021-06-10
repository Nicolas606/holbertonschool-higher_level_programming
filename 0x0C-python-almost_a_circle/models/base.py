#!/usr/bin/python3
""" Module: base.py """
import json


class Base:
    """ This class will be the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        new_file = cls.__name__ + '.json'
        list_empty = []
        if list_objs != None:
            for objs in list_objs:
                list_empty.append(objs.to_dictionary())
        with open(new_file, 'w') as file:
            file.write(cls.to_json_string(list_empty))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == []:
            return '[]'
        else:
            return json.loads(json_string)
