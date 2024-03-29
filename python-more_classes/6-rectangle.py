#!/usr/bin/python3
"""rectangle modul"""


class Rectangle:
    """class that defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init new rectangle with his width and heigth"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ define the area of a rectangle entrer in argument"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ define the perimeter of a rectangle entre in arg"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """init print of rect"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for line in range(self.__height - 1):
            print("#" * self.__width)
        return ("#" * self.__width)

    def __repr__(self):
        """def repr print"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """def del print"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
