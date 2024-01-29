#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        if len(tuple_b) >= 2:
            newtuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
        elif len(tuple_b) == 1:
            newtuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1]))
        else:
            return tuple_a
    elif len(tuple_a) == 1:
        if len(tuple_b) >= 2:
            newtuple = ((tuple_a[0] + tuple_b[0]), (tuple_b[1]))
        elif len(tuple_b) == 1:
            newtuple = ((tuple_a[0] + tuple_b[0]),)
        else:
            return tuple_a
    else:
        return tuple_b
    return newtuple
