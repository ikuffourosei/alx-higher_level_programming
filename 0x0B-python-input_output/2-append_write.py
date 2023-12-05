#!/usr/bin/python3

"""The append write module
"""


def append_write(filename="", text=""):
    """A function that appends a text to a file;
    creates the file if it does not exist
    """
    with open(filename, "a+", encoding="UTF-8") as af:
        file_append = af.write(text)
        return file_append
