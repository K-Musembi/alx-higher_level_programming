#!/usr/bin/python3

class Square:
    '''A class that defines a sqaure with an attribute and methods.'''

    def __init__(self, size=0):
        '''A method that creates objects of the class.

        Args:
            size (int): integer type.

        Attributes:
            size (int): integer type.

        '''

        self.__size = size

    @property
    def size(self):
        '''A method to get the private attribute.

        Returns:
            Attribute.

        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''A method to set the value of the attribute.

        Args:
            value (int): integer type

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.

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
            Area.

        '''

        return self.__size * self.__size

    def my_print(self):
        '''A method that prints a square using #.'''

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")

                print()
