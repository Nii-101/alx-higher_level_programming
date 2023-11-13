#!/usr/bin/python3
""" A square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class square that prints a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Calling the super class with: id, x, y, width and height"""
        super().__init__(size, size, x, y,  id)

    def __str__(self):
        """Overloading the __str__ method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """"Getting the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting the size of the square"""
        self.width = value
        self.height = value
