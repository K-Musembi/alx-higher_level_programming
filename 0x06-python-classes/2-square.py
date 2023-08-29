#!/usr/bin/python3

class Square:
    '''A class that defines a square.

    '''

    def __init__(self, size=0):
        '''A method to initialize the class objects.

        Args:
            size (int): integer type.

        Attributes:
            size (int): integer type.

        Raises:
            TypeError: size not an integer.
            ValueError: size less than zero.

        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
