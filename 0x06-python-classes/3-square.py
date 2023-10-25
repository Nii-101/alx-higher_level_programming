#!/usr/bin/python3
'''A class defining a square'''

class Square:
    ''' A class defining a square'''
    def __init__(self, size=0):
        ''' Initializing the class Square
        Args: size=0: the size of the square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if 0 > size:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        ''' Calculating the area of the square)'''
        return(self.__size ** 2)
