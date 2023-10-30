#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """Defining a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Args: width = width of the rectangle;
              height = height of the rectangle;
        """

        self.__height = height
        self.__width = width

    @property
    def width(self, width=0):
        """ A getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ A setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, height=0):
        """A getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
