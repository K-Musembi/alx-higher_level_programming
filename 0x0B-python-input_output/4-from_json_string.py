#!/usr/bin/python3
'''Function to return Python object'''

import json


def from_json_string(my_str):
    '''Return object represented by JSON string'''

    return json.loads(my_str)
