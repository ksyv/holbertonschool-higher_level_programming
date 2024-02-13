#!/usr/bin/python3
"""modul write a class that inherits from another"""


class MyList(list):
    """prints the list sorted in ascending sort"""
    def print_sorted(self):
        """prints the list sorted in ascending sort"""
        print(sorted(self))
