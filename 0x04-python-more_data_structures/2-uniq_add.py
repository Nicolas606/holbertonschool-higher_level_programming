#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = list(set(my_list))
    return sum(copy)
