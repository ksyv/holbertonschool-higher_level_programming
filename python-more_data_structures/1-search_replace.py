#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index in my_list:
        if index is not search:
            new_list.append(index)
        else:
            new_list.append(replace)
    return new_list
