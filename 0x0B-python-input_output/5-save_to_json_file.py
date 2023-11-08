#!/usr/bin/python3
""" Writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file"""
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
