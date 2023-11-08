#!/usr/bin/python3
""" Writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    x = json.dumps(my_obj)
    with open(filename, "w") as f:
        return f.write(x)
