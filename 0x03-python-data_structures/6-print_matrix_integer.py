#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first_matrix in matrix:
        for second_matrix in first_matrix:
            if second_matrix != first_matrix[-1]:
                print("{:d} ".format(second_matrix), end='')
            else:
                print("{:d}".format(second_matrix), end='')
        print('')
