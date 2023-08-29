#!/usr/bin/python3

class Square:
    '''A class that defines a square.
    It contains one attribute but no
    methods.

    '''

    def __init__(self, size):
        '''The __init__ method is used to
        initialize the objects.

        Args:
            size (int): integer type, number

        Attributes:
            __size (int): private, integer type.

        '''

        self.__size = size
