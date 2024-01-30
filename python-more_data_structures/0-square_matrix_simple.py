#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    return [[integer ** 2 for integer in firstlevel] for firstlevel in matrix]
