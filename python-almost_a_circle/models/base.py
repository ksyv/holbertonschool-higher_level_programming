#!/usr/bin/python3
"""modul for create a Base class"""


class Base:
    """Base class mother of all other clss of this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Manage the id attribute for all classes

        Args:
            id: id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
