#!/usr/bin/python3
""" Module: appends a string at the end of a text file (UTF8) and returns the
number of characters added """


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file and returns the
number of characters added """
    with open(filename, 'a', encoding='utf-8') as new_file:
        return new_file.write(text)
