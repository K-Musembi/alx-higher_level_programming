#!/usr/bin/python3
'''A module that defines two classes, Node and SinglyLinkedList.'''


class Node:
    '''A class that defines a node.'''

    def __init__(self, data, next_node=None):
        '''A method to initialize class objects.

        Args:
            data (int): integer type.
            next_node (Node): Node type.

        Attributes:
            data (int): integer type.
            next_node (Node): Node type.

        '''

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''A method to get the private field.

        Returns:
            data attribute.

        '''

        return self.__data

    @data.setter
    def data(self, value):
        '''A method to set the field value.

        Args:
            value (int): integer type.

        Raises:
            TypeError: if value is not an integer.

        '''

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        '''A method to get the private field.

        Returns:
            next_node attribute.

        '''

        return self.__next_node

    def next_node(self, value):
        '''A method to set the field value.

        Args:
            value (Node): Node type.

        Raises:
            TypeError: if value is not Node object or None.

        '''

        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    '''A class that defines a singly linked list.'''

    def __init__(self):
        '''A method to initialize class objects.

        Attributes:
            head (Node): Node type.

        '''

        self.__head = None

        current = self.__head
        while (current):
            print(current.__data)
            current = current.__next

    def sorted_insert(self, value):
        '''A method to insert nodes in a sorted manner.

        Args:
            value (int): integer type.

        '''

        new_node = Node(value)

        if not self.__head:
            self.__head = new_node
        else:
            current = self.__head
            
            if value <= current.__data:
                new_node.__next = current
                self.__head = new_node
            else:
                while current.__next:
                    if current.__data < value <= current.__next.__data:
                        new_node.__next = current.__next
                        current.__next = new_node
                        break
                    current = current.__next
                if current.__next == None:
                    current.__next = new_node
