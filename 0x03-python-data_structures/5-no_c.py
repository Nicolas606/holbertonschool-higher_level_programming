#!/usr/bin/python3
def no_c(my_string):
    delete = {67 : 26, 99 : 26}
    return my_string.translate(delete)
