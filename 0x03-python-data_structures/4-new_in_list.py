#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    length = len(my_list)
    for i in range(length):
        copy.append(my_list[i])
        if idx < 0:
            return my_list
        if idx > (length - 1):
            return (copy)
    copy[idx] = element
    return (copy)
