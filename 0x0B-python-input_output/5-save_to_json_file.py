#!/usr/bin/python3
""" Module: writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """  function that writes an Object to a text file, using a JSON
representation """
    with open(filename, 'w') as new_file:
        json.dump(my_obj, new_file)
