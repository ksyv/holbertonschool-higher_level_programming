#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv[1:]
    numberOfArgs = len(args)
    if (numberOfArgs == 0):
        print("0 arguments.")
    elif (numberOfArgs == 1):
        print("1 argument:")
    else:
        print(f"{numberOfArgs} arguments:")
    for index in range(numberOfArgs):
        print(f"{index + 1}: {args[index]}")