#!/usr/bin/python3
import calculator_1 as c


def star():
	a = 10
	b = 5
	print("{} + {} = {}".format(a, b, c.add(a, b)))
	print("{} - {} = {}".format(a, b, c.sub(a, b)))
	print("{} * {} = {}".format(a, b, c.mul(a, b)))
	print("{} / {} = {}".format(a, b, c.div(a, b)))

if __name__ == "__main__":
    star()
