#!/usr/bin/python3
'''Defines a base class'''

import json


class Base:
    '''The base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize class objects'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSON string representation'''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []

        return json.dumps(list_dictionaries, default=vars)

    @classmethod
    def save_to_file(cls, list_objs):
        '''JSON string to file'''

        with open("Rectangle.json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                j_string = Base.to_json_string(list_objs)
                f.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        '''JSON string to list'''

        if json_string is None or json_string == " ":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Set instance attributes'''

        obj = cls(1, 2)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''From JSON to list of instances'''

        try:
            with open("Rectangle.json", encoding="utf-8") as file:
                str_obj = file.read()
        except Exception:
            pass

        if not file:
            return []

        '''my_str = Base.from_json_string(str_obj)
        my_list = Base.create(my_str)

        return my_list'''
