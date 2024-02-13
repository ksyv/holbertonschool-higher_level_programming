#!/usr/bin/python3
"""modul for search all available attributes and methode of an object"""


def lookup(obj):
    """return list of attributes and methods of an object
    arg: obj is the object
    return: the list
    """
    return dir(obj)
