#!/usr/bin/python3
'''Send request and display Id
'''

import requests
import sys


url = sys.argv[1]

response = requests.get(url)

if "X-Request-Id" in response.headers:
    x_id = response.headers["X-Request-Id"]

print(f"{x_id}")


def main():
    '''Empty function'''
    ...


if __name__ == "__main__":
    main()
