#!/usr/bin/python3
"""Module for creation of a class "rectangle" """
from models.base import Base


class Rectangle(Base):
    """define the Rectangle class inherit from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """create and protect attributes for the rectangle instance

        Args:
            width
            height
            x Defaults to 0.
            y Defaults to 0.
            id Defaults to None, assign by Base id logic.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ def width in private attribute
        check if it's a positive integer"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieve height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ def height in private attribute
        check if it's a positive integer"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrieve x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ def x in private attribute
        check if it's a positive integer or 0"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieve y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ def y in private attribute
        check if it's a positive integer or 0"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ define the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """print rectangle instance with "#" """
        for index in range(self.height):
            print("#" * self.width)
