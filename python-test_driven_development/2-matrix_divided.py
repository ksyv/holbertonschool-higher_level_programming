#!/usr/bin/python3
"""modul for the task: Write a function \
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of the matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    temporary_array = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError('matrix must be \
                                a matrix (list of lists) of integers/floats')
            temporary_array.append(round(number / div, 2))
        new_matrix.append(temporary_array)
        temporary_array = []
    return new_matrix


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
