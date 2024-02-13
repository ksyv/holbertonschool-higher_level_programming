#!/usr/bin/python3
"""Write a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size and validate with integer validator"""
    def __init__(self, size):
        """init and check if size is integer"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
