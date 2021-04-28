#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = len(argv) - 1

    if counter == 0:
        print('0')
    if counter == 1:
        print("{}".format(argv[1]))
    if counter > 1:
        sum = 0
        for result in argv[1:]:
            sum += int(result)
        print(sum)
