#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace an element from a list
        my_list is the original list
        idx is the index of replaced element
        element is the new element at the index"""
    if idx < 0 or idx > len(my_list) - 1:
        # if idx is negative or out of range, return None
        return my_list
    new_list = my_list
    new_list[idx] = element
    return new_list  # return value of element in idx
