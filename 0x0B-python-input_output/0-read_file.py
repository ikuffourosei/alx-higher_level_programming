#!/usr/bin/bash

"""The read file module
Reads a file
"""
def read_file(filename=""):
    with open(filename, 'r', encoding='UTF-8') as rf:
        file_read = rf.read()
    return file_read
