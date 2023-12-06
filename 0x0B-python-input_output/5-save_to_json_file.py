#!/usr/bin/python3
"""save_to_json module
"""


import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to a text file
    using JSON representation
    """
    with open(filename, "w", encoding="UTF-8") as wf:
        text = json.dumps(my_obj)
        save_file = wf.write(text)
        return save_file
