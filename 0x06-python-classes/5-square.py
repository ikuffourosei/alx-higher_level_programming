#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square class
    Attributes:
        __size (int): size of the square
    Method:
    area: calculates the area
    """
    def __init__(self, size=0):
        """
        initializes the square
        Args:
            size (int): size of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        calculates the area of the square
        Returns:
            int: The sqaured value of __size
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of a side of the square square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """
        prints the square
        Arguments:
            None
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for num in range(self.__size):
            print("".join(["#" for x in range(self.__size)]))
