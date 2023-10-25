#!/usr/bin/python3
''' A class defining a square '''

class Square:
    ''' A class defining a square '''
    def __init__(self, size=0):
        ''' Initializing the class Square
        Args: size=0: The size of the square
        '''
        self.__size = size

    @property
    def size(self):
        ''' Getting the size of the square '''
        return self.__size

    @size.setter
    def size(self,value):
        ''' Setting the size of the square '''

        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        ''' Returns the current square area '''

        return (self.__size ** 2)
