#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first_level in matrix:
        for integer in first_level:
            print("{:d}".format(integer), end =" ")
        print("")
