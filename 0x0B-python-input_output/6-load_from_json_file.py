#!/usr/bin/python3
"""The load_from_json_file module
"""


import json


def load_from_json_file(filename):
    """function that creates an object from a json file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        file_read = f.read()
        file_contents = json.loads(file_read)
        return file_contents
