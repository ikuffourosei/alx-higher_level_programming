#!/usr/bin/python3
"""The to_json_string module
"""


import json


def to_json_string(my_obj):
    """Function that returns a string in the JSON format
    """
    return json.dumps(my_obj)
