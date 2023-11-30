#!/usr/bin/python3

"""A module to say my name
"""

def say_my_name(first_name, last_name=""):
    """
    A function that takes in two arguments and prints a sentence saying
    My name is ''first_name'' ''last_name''
    Args:
        first_name: string
        last_name: string
    Return:
        A sentence: string
    Raise:
        TypeError: If ''first_name'' and ''last_name'' are not of type(string)
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
