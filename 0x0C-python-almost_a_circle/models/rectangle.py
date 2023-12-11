#!/usr/bin/python3
""" A class Rectangle that inherits from a class Base
"""

from .base import Base


class Rectangle(Base):
    """ Initiating the rectangle with private instance attributes
    and a getter and setter for each attribute
    Methods:
        area: returns the area of the rectangle
        display: writes the # symbol to the stdout
        __str__: overrrides the '__str__' method
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the class constructor
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinates of the recatngle
            y (int): y coordinates of the rectangle
            id (int): id of the rectangle
        Raise:
            TypeError: if width, heigth, x, or y is not int
            ValueError: if width and height <= 0, if x and y < 0
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getting the width"""
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) != int:
            raise TypeError('width must be an integer')
        if new_width <= 0:
            raise ValueError('width must be > 0')
        self.__width = new_width

    @property
    def height(self):
        """getting the height"""
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) != int:
            raise TypeError('height must be an integer')
        if new_height <= 0:
            raise ValueError('height must be > 0')
        self.__height = new_height

    @property
    def x(self):
        """getting the x coordinate"""
        return self.__x

    @x.setter
    def x(self, x_value):
        if type(x_value) != int:
            raise TypeError('x must be an integer')
        if x_value < 0:
            raise ValueError('x must be >= 0')
        self.__x = x_value

    @property
    def y(self):
        """getting the y coordinate"""
        return self.__y

    @y.setter
    def y(self, y_value):
        if type(y_value) != int:
            raise TypeError('y must be an integer')
        if y_value < 0:
            raise ValueError('y must be >= 0')
        self.__y = y_value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.width * self.height
    
    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.height == 0 or self.width == 0:
            print("")
            return
        
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x + "#" * self.width)
    
    def __str__(self):
        """overriding the '__str__'method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
