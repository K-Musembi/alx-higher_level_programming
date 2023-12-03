#!/usr/bin/python3
"""Display GitHub user id
"""

import requests
import sys


url = "https://api.github.com/user"

response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

info = response.json()

if info:
    print(f"{info.get('id')}")


def main():
    '''Empty function'''
    ...


if __name__ == "__main__":
    main()
