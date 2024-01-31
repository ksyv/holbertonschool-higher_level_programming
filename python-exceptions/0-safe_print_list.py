#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_number = 0
    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end="")
            real_number += 1
        except IndexError:
            break
    print("")
    return real_number
