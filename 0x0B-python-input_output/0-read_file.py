#!/usr/bin/python3
"""The ''read_file''
"""


def read_file(filename=''):
    """Reads a file and prints to stdout"""
    with open(filename, 'r', encoding='UTF-8') as rf:
        print(rf.read())
