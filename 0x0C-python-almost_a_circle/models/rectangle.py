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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        """x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setting the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle"""
        return self.width * self.height

    def display(self):
        """ Prints the rectangle to standard out"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Overriding the __str__ method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id,self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]

            if len(args) > 1:
                self.width = args[1]

            if len(args) > 2:
                self.height = args[2]

            if len(args) > 3:
                self.x = args[3]

            if len(args) > 4:
                self.y = args[4]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
