#!/usr/bin/python3
'''Defines a class'''


class Rectangle:
    '''A rectangle class'''

    def __init__(self, width=0, height=0):
        '''To initialize objects'''

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Get width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Set width'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''Get height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Set height'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''Calculates rectangle area'''

        return self.__height * self.__width

    def perimeter(self):
        '''Calculates rectangle perimeter'''

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__height + self.__width) * 2

    def __str__(self):
        '''Return a string'''

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        '''Return a string representation'''

        return f"Rectangle(width={self.__width}, height={self.__height})"
