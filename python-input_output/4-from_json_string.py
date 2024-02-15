#!/usr/bin/python3
"""module for define a function who return an object with json string """
import json


def from_json_string(my_str):
    """return an object with json string"""
    return json.loads(my_str)
