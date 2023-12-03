#!/usr/bin/python3
'''Display response as JSON string'''

import requests
import sys


if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

url = "http://0.0.0.0:5000/search_user"

letter = {'q': q}

response = requests.post(url, data=letter)

try:
    r_json = response.json()
    if r_json:
        print(f"[{r_json['id']}] {r_json['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")


def main():
    '''Empty function'''
    pass


if __name__ == "__main__":
    main()
