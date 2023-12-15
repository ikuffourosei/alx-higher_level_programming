#!/usr/bin/python3
""" A class called Base
"""


import json


class Base:
    """ initating the Base class with a private class attribute
    """
    __nb_objects = 0    # class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serializes or Converts a list of dictionary object to json string
        Args:
            list_dictionaries (list)
        Return:
            json_string (str)
        """
        if list_dictionaries is not None or list_dictionaries != "[]":
            json_string = json.dumps(list_dictionaries)
            return json_string
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of class objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as wf:
            if list_objs is not None:
                dict_list = [items.to_dictionary() for items in list_objs]
                wf.write(Base.to_json_string(dict_list))
            else:
                wf.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Deserializes a JSON string and returns the original format.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            [] (list): if json_string is "None"
            Otherwise: original object format
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
