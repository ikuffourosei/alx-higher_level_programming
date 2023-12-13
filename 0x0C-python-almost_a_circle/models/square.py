#!/usr/bin/python3
"""A class that behaves like a square
Inherits its properties from a rectangle"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Initiating a square
    Inherits all properties and methods from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the '__str__'method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
