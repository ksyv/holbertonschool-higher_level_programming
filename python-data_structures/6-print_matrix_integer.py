#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first_level in matrix:
        for integer in range(0, len(first_level)):
            if integer < len(first_level) - 1:
                print("{:d}".format(first_level[integer]), end=" ")
            else:
                print("{:d}".format(first_level[integer]), end="")
        print("")
