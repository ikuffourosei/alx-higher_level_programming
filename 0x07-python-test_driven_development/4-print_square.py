#!/usr/bin/python3

"""print square module
"""
def print_square(size):
    """
    a function that prints a square with the character #
    Args:
        size: int
    Return:
        size of square with #: string
    Raise:
        TypeError: size must be an integer
        ValueError: size must not be less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    count = 0
    while count < size:
        print("#" * size)
        count += 1
