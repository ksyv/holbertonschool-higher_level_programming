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
