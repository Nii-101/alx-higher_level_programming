#!/usr/bin/python3
""" A base class for all other classes in this project"""
import json


class Base:
    """A base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor for the class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
         of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs
         to a file"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)
