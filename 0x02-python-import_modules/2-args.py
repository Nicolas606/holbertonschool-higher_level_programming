#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    contador = len(argv) - 1
    if contador == 0:
        print("0 arguments")
    if contador == 1:
        print("1 argument:")
        print("{}: {}".format(contador, argv[1]))
    if contador > 1:
        print("{} arguments:".format(contador))
        for contador in range(1, contador + 1):
            print("{}: {}".format(contador, argv[contador]))
