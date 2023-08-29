#!/usr/bin/python3

'''A module that defines a class with its attributes and methods.'''


class Square:
    '''A class that defines a square with attribute and method.

    '''

    def __init__(self, size=0):
        '''A method that initializes class objects.

        Args:
            size (int): integer type.

        Attributes:
            size (int): integer type.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.

        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''An instance method to compute area of the square.

        Returns:
            Area of square.

        '''

        return self.__size * self.__size
