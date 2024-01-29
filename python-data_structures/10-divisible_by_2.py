#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_string = []  # add new string and initialize
    for index in my_list:
        if index % 2 == 0:
            new_string.append(True)
        else:
            new_string.append(False)
    return new_string
