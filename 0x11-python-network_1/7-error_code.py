#!/usr/bin/python3
'''Print 'error code' if status greater than 400
'''

import requests
import sys


url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(f"{response.text}")


def main():
    '''Empty function'''
    ...


if __name__ == "__main__":
    main()
