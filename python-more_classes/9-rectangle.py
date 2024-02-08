#!/usr/bin/python3
"""rectangle modul"""


class Rectangle:
    """class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init new rectangle with his width and heigth"""
        self.width = width
        self.height = height
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
            print(str(self.print_symbol) * self.__width)
        return (str(self.print_symbol) * self.__width)

    def __repr__(self):
        """def repr print"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """def del print"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new rectangle with width = height = size"""
        return cls(size, size)
