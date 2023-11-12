#!/usr/bin/python3
""" A rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ A class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing the class
            Args: width, height, x, y, id
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """width getter and setter"""
    @property
    def width(self):
        """getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """height getter and setter"""
    @property
    def height(self):
        """getting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """x getter and setter"""
    @property
    def x(self):
        """getting x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setting the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """y getter and setter"""
    @property
    def y(self):
        """getting the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle to standard out"""
        for a in range(self.__height):
            for b in range(self.__width):
                print("#", end="")
            print()