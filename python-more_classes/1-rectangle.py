#!/usr/bin/python3
"""square modul"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """init new rectangle with his width and heigth"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
