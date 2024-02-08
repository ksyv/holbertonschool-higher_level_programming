#!/usr/bin/python3
"""Modul for print a square"""


def print_square(size):
    """Check if size is a positiv integer and print # square"""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")
    for edge in range(size):
        print("#" * size)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
