#!/usr/bin/python3
"""Module: text_identation"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after each of these
characters: ., ? and : """
    if type(text ) != str:
        raise TypeError("text must be a string")

    new_line = ''
    for letter in text:
        new_line += letter
        if letter in '.?:':
            new_line += '\n\n'
    print(new_line.strip(), end='')
    print()
