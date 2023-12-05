#!/usr/bin/python3

"""The write file module
"""


def write_file(filename="", text=""):
    """A function that writes a text to a string"""
    with open(filename, "w", encoding="UTF-8") as wf:
        file_write = wf.write(text)
        return file_write
