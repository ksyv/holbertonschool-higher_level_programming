#!/usr/bin/python3
"""module for define a function who retur json representation of an object"""
import json


def to_json_string(my_obj):
    """return json representation of a string"""
    return json.dumps(my_obj)
