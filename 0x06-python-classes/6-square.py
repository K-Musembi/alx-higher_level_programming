#!/usr/bin/python3

'''A module that defines a class with its attributes and methods.'''


class Square:
    '''A class that defines a square with attributes and methods.'''

    def __init__(self, size=0, position=(0, 0)):
        '''A method that initializes class objects.

        Args:
            size (int): integer type.
            position (int): integer type.

        Attributes:
            size (int): integer type.
            position (int): integer type.

        '''

        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''A method to get the private attribute.

        Returns:
            Size attribute.

        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''A method to set the value of the attribute.

        Args:
            value (int): integer type.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.

        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        '''A method to retrieve the private attribute.

        Returns:
            Position attribute.

        '''

        return self.__position

    @position.setter
    def position(self, value):
        '''A method to set the value of the attribute.

        Args:
            value (int): integer type.

        Raises:
            TypeError: value is not an integer.

        '''

        if len(value) != 2 or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0]) or not isinstance(value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        '''A method that computes the area of the square.

        Returns:
            Area of square.

        '''

        return self.__size * self.__size

    def my_print(self):
        '''A method that prints a square using #.'''

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if j == 0:
                        for k in range(self.__position[0]):
                            print("_", end="")
                    print("#", end="")
                print()
