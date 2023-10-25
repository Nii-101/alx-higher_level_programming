#!/usr/bin/python3
''' A class that defines a square '''



class Square:
    ''' A class that defines a square '''
    def __init__(self, size=0):
        ''' Initializing the square class
        Args: size=0 is the square size
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
