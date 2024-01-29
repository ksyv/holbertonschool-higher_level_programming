#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order
        my_list is the integer's list"""
    for index in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[index]))
