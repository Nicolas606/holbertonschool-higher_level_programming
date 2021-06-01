#!/usr/bin/python3
""" Module: that creates an Object from a “JSON file” """

import json


def load_from_json_file(filename):
    """  function that creates an Object from a “JSON file” """
    with open(filename, 'r', encoding="utf-8") as new_file:
        return json.loads(new_file)
