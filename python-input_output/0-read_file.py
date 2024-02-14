#!/usr/bin/python3
"""_summary_"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as file:
        readFile = file.read()
        print(readFile)
