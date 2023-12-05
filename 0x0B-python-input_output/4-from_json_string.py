#!/usr/bin/python3
"""The ''from_json_string'' module
"""


import json


def from_json_string(my_str):
    """function that converts JSON format data to the original data structure
    """
    return json.loads(my_str)
