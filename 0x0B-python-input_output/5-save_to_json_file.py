#!/usr/bin/python3
'''Function - writes object to file'''

import json


def save_to_json_file(my_obj, filename):
    '''Write to file as JSON'''

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
