#!/usr/bin/python3

"""Defining a Square"""


class Square:
    """Square class
    Attributes:
        __size (int): size of the square
    Method:
        area: calculates the area of the square

    """
    def __init__(self, size=0):
        """
        initializing the square
        Args:
            size (int): size of the square
        Returns:
            None
        Raises:
            ValueError: If 'size' is less than 0
            TypeError: If 'size' is not an integer
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        defines the area of the square
        Args:
            None
        Returns:
            int: the squared value of __size
        """
        result = self.__size ** 2
        return result
