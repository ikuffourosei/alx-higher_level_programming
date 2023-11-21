#!/usr/bin/python3

""" Defining a Square """



class Square:
    
    """ A class Square with a private size attribute

    Attributes:
        __size (int): size of the square

    """
    def __init__(self, size):

        """Initializing the class

        Args: 
            size (int): size of the square

        Returns: None

        """
        self.__size = size
