#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = len(argv) - 1
    if counter == 0:
        print("0 arguments.")
    if counter == 1:
        print("1 argument:")
        print("{}: {}".format(counter, argv[1]))
    if counter > 1:
        print("{} arguments:".format(counter))
        for counter in range(1, counter + 1):
            print("{}: {}".format(counter, argv[counter]))
