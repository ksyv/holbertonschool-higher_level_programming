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

    @property
    def size(self):
        """retrieve size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """ def size in public attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute"""

        if args is not None and len(args) != 0:
            listOfArg = []
            for arg in args:
                listOfArg.append(arg)
            try:
                self.id = listOfArg[0]
                self.size = listOfArg[1]
                self.x = listOfArg[2]
                self.y = listOfArg[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
