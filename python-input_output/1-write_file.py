#!/usr/bin/python3
"""_summary_"""


def write_file(filename="", text=""):

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
