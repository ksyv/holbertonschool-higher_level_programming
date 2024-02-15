#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student():
    """Defines the Student class"""
    def __init__(self, first_name, last_name, age):
        """Creates a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__

        new_dic = {}
        for i in attrs:
            try:
                new_dic[i] = self.__dict__[i]
            except Exception:
                pass

        return new_dic
