#!/usr/bin/python3
def no_c(my_string):
    delete = {67: 127, 99: 127}
    new_string = my_string.translate(delete)
    return new_string
