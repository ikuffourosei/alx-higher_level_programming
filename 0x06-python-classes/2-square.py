#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """A class square with private instance variable

    Attributes:
        __size (int): size of the square

    """
    def __init__(self, size=0):
        """
        Args:
            size (int): size of the square
        Returns:
            None
        Raises:
            ValueError: If 'size' is less than 0
            TypeError: If 'size' is not an integer
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size
