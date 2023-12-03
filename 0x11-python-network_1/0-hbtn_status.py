#!/usr/bin/python3
""" Fetch data and print response
"""

import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    utf_8 = body.decode("utf-8")

print("Body response:")
print("\t- type", type(body))
print("\t- content", body)
print("\t- utf8 content:", utf_8)


def main():
    """ Empty function """
    ...


if __name__ == "__main__":
    main()
