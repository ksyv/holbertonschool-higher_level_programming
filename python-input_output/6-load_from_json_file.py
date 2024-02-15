#!/usr/bin/python3
"""module for define a function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """that creates an Object from a “JSON file”"""
    with open(filename, 'w', encoding="utf-8") as file:
        return json.load(file)
