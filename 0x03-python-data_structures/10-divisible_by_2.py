#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    copy = []
    i = 0
    while i < length:
        if my_list[i] % 2 == 0:
            copy.append(True)
        else:
            copy.append(False)
        i += 1
    return copy
