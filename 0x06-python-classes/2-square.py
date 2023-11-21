#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """A class square with private instance variable

    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Instantiation with optional size

        Args:
            size (int): size of the square
        Returns:
            None
        Raises:
            TypeError: If the type of the size is not an int
            ValueError: if size is less than 0, then the sqaure is invalid
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size
