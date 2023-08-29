#!/usr/bin/python3

class Square:
    '''A class that defines and initializes a sqaure.'''

    def __init__(self, size=0):
        '''A method that initializes objects.

        Args:
            size (int): integer type.

        Attributes:
            size (int): integer type.

        '''

        self.__size = size

    @property
    def size(self):
        '''A methgd to get the private instance attribute.

        Returns:
            Attribute.

        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''A method to set the private attribute value.

        Args:
            value (int): integer type.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.

        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''A method to compute the area of the sqaure.

        Returns:
            Area of sqaure.

        '''

        return self.__size * self.__size
