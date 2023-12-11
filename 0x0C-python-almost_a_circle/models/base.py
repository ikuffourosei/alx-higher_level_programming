#!/usr/bin/python3
""" A class called Base
"""


class Base:
    """ initating the Base class with a private class attribute
    """
    __nb_objects = 0    # class attribute

    def __init__(self, id=None):
        if not id:
            self.id = id
        self.id = Base.__nb_objects + 1
