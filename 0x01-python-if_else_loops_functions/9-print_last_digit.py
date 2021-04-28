#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_number = ((number * -1) % 10)
        print("{}".format(last_number), end="")
        return last_number
    else:
        last_number = number % 10
        print("{}".format(last_number),end="")
        return last_number
