#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy[i] = replace
    return copy
