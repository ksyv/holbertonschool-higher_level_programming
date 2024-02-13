#!/usr/bin/python3
"""write a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print rectangle width/height"""
        return '[Rectangle] ' + str(self.__width) + "/" + str(self.__height)
