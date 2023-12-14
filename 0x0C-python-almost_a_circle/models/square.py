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
        """overriding the '__str__' method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Setting the height and width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute

        1st argument should be the 'id' attribute
        2nd argument should be the 'width' attribute
        3rd argument should be the 'height' attribute
        4th argument should be the 'x' attribute
        5th argument should be the 'y' attribute

        Args:
            *args (list): positional arguments
            **kwargs (dict): key-worded arguments
        """
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "size":
                    self.size =  val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val
