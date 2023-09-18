#!/usr/bin/python3
'''Script to add args to list'''

from sys import argv
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

lst = []

with open('add_item.json', 'w+', encoding='utf-8') as f:
    lst = load_from_json_file(f)

    for arg in argv[1:]:
        lst.append(arg)

    save_to_json_file(lst, f)
