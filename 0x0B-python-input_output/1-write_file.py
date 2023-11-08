#!/usr/bin/python3
"""A function that writes a string to a text file
    and returns the number of characters written"""


def write_file(filename="", text=""):
    """ Writes a string to a UTF """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
