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
        for blankline in range(self.y):
            print("")
        for index in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''Overwritting the str method'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute"""

        if args is not None and len(args) != 0:
            listOfArg = []
            for arg in args:
                listOfArg.append(arg)
            try:
                self.id = listOfArg[0]
                self.width = listOfArg[1]
                self.height = listOfArg[2]
                self.x = listOfArg[3]
                self.y = listOfArg[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
