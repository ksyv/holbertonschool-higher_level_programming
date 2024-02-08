#!/usr/bin/python3
"""modul for the task: Write a function that prints\
a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """run text and replace specfied char and space by 2 new line"""
    if not isinstance(text , str):
        raise TypeError("text must be a string")
    specify_char = ['.', '?', ':', ',']
    first_char = 0
    index = 0
    for test_char in text:
        if test_char in specify_char:
            char_index = index + 1
            print("{}\n".format(text[first_char:char_index]))
            first_char = char_index + 1
        index += 1

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
