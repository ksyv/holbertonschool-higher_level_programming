#!/usr/bin/python3
"""modul for create a class square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define the square class inherit from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class with logic of __init__ Rectangle
        width and height must be assigned to the value of size"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Overwritting the str method'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
