#!/usr/bin/python3

""" Defining a Square """



class Square:
    
    """ A class Square that defines a Square with a private size attribute

    Attributes: 
              __size (int)

    """
    def __init__(self, size):

        """Initializing the class

        Args: 
             size (int): size of the square

        Return: None

        """
        self.__size = size
