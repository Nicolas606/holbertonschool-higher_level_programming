#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: {}".format(a / b))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
    finally:
        if b == 0:
            return None
        else:
            return (a / b)
