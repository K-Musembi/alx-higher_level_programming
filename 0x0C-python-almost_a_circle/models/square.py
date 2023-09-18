#!/usr/bin/python3
'''Defines the square class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize class objects'''

        super().__init__(size, size, x, y, id)
        Rectangle.width.fset(self, size)
        Rectangle.height.fset(self, size)
        Rectangle.x.fset(self, x)
        Rectangle.y.fset(self, y)

    def __str__(self):
        '''String representation'''

        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''Get size'''

        return self.width

    @size.setter
    def size(self, size):
        '''Set size'''

        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''Assign instance attributes'''

        if args and args[0] is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if value is not None:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Object to dictionary'''

        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
