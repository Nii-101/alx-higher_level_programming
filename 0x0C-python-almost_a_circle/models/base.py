#!/usr/bin/python3
""" A base class for all other classes in this project"""


class Base:
    """A base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor for the class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
