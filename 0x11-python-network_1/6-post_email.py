#!/usr/bin/python3
'''POST url and email and display response
'''

import requests
import sys


post_data = {"email": sys.argv[2]}

response = requests.post(sys.argv[1], data=post_data)

print(f"Your email is: {response.text}")


def main():
    '''Empty function'''
    ...


if __name__ == "__main__":
    main()
