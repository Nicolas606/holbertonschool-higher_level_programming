#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    length = len(my_list)
    for i in range(length - 1):
        copy.append(my_list[i])
    copy[idx] = element
    return (copy)
