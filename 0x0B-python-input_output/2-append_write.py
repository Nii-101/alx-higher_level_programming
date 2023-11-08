#!/usr/bin/python3
"""
    A function that appends a string to the end of a text file
    and returns the number of characters
"""


def append_write(filename="", text=""):
    """ Appends a string to a text file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
