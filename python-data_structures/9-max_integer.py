#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    max = 0
    for integer in my_list:
        if max < integer:
            max = integer
    return max
