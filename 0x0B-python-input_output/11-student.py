#!/usr/bin/python3
""" Defines a class student """


class Student:
    """ Defines a class Student """
    def __init__(self, first_name, last_name, age):
        """Inititializing the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieve dictionary representation of class Student """
        if type(attrs) == list and all(type(a) == str for a in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of student """
        for i in json:
            self.__dict__.update({i: json[i]})                        
