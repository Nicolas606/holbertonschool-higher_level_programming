#!/usr/bin/python3
"""Module: Reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout """

    with open(filename, 'r', encoding='utf-8') as new_file:
        print(new_file.read(), end='')
