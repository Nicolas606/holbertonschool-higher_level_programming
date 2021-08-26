#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    length = len(my_list)
    for i in range(length):
        copy.append(my_list[i])
        if idx < 0 or idx > (length - 1):
            return my_list
    copy[idx] = element
    return (copy)
