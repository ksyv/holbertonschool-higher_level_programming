#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """ Write a class BaseGeometry (based on 6-base_geometry.py).
    """
    def area(self):
        """ that raises an Exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value

        Args:
            name (_type_):  is always a string
            value (_type_): do is an integer up to 0

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
