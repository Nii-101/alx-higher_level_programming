#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """Defining a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Args: width = width of the rectangle;
              height = height of the rectangle;
        """

        self.height = height
        self.width = width

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
        if type(value) != int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public instance for area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """A public instance for perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return ((("#" * self.__width) + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Print the rectangle using eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
