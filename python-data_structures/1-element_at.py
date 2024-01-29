#!/usr/bin/python3
def element_at(my_list, idx):
    """retrives an element from a list
        my-list is the list
        idx is the searched element"""
    if idx < 0 or idx > len(my_list) - 1: #if idx is negative or out of range, return None
        return
    return my_list[idx] #return value of element in idx
    