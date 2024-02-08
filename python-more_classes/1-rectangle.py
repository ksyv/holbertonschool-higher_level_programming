#!/usr/bin/python3
"""rectangle modul"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """init new rectangle with his width and heigth"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """def if width is an int >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """def if height is an int >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
