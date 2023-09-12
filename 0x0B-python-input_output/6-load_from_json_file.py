#!/usr/bin/python3
'''Function to create object from JSON file'''

import json


def load_from_json_file(filename):
    '''Create object from JSON'''

    with open(filename, 'r', encoding='utf-8') as f:
        x = json.load(f)
        return x
