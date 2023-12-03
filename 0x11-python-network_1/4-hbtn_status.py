#!/usr/bin/python3
"""Fetch URL and display response
"""


import requests

response = requests.get("https://alx-intranet.hbtn.io/status")

body = response.text

print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")


def main():
    '''Empty function'''
    ...


if __name__ == "__main__":
    main()
