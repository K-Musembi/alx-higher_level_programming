#!/usr/bin/python3
'''Defines a class'''


class Rectangle:
    '''A rectangle class'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''To initialize objects'''

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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
            return '\n'.join(Rectangle.print_symbol * self.__width
                             for _ in range(self.__height))

    def __repr__(self):
        '''Return a string representation'''

        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __del__(self):
        '''Delete instance'''

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns biggest rectangle based on area'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''Returns new class instance'''

        width = size
        height = size
        return cls(width, height)
