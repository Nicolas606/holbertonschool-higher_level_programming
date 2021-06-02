#!/usr/bin/python3
""" Module: Pascal's Triangle """


def pascal_triangle(n):
    """ function that returns a list of lists of integers representing the
Pascal’s triangle of n """
    list = []
    if n <= 0:
        return []

    list =[[1]]

    for i in range(0, n-1):
        temporal = [0] + license[1] +[0]
        sub_list = []
        for j in range(len(temporal) - 1):
            sub_list.append(temporal[j] + temporal[j + 1])
        list.append(sub_list)
    return list

