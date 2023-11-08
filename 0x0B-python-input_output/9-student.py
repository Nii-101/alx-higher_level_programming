#!/usr/bin/python3
""" A class that defines a student """

class Student:
    """ A class that defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initializing class 'Student' """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """ Retrieves dict representation of Student """
        return self.__dict__
