#!/usr/bin/python3
'''Defines a child class'''

from models.base import Base


class Rectangle(Base):
    '''A rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize class object'''

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        '''Get width'''

        return self.__width

    @width.setter
    def width(self, width):
        '''Set width'''

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        '''Get height'''

        return self.__height

    @height.setter
    def height(self, height):
        '''Set height'''

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        '''Get x'''

        return self.__x

    @x.setter
    def x(self, x):
        '''Set x'''

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        '''Get y'''

        return self.__y

    @y.setter
    def y(self, y):
        '''set y'''

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        '''Area value of instance'''

        return self.__width * self.__height

    def display(self):
        '''Prints rectangle instance'''

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        '''String representation'''

        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} \
                - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        '''Assign argument to attribute'''

        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if value is not None:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Object to dictionary'''

        return {'x': self.__x, 'y': self.__y, 'id': self.id, 'height':
                self.__height, 'width': self.__width}
