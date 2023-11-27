#!/usr/bin/python3
"""Add_integer module"""

def add_integer(a, b=98):
    """
    A fucntion that adds two integers ''a'' and ''b''.

    Args:
        a (int or float)
        b (int or float)
    Return:
        The sum of ''a'' and ''b''
    Raises:
        TypeError: If ''a'' and ''b'' are not integers nor floats.
    """
    #check if a and b are neither floats nor integers
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    #convert a and b to integers
    a = int(a)
    b = int(b)

    return a + b
