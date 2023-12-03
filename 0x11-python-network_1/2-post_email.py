#!/usr/bin/python3
""" POST email and display response
"""

import urllib.request
import urllib.parse
import sys


data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")

req = urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")

print(f"Your email is: {body}")


def main():
    """Empty function"""
    ...


if __name__ == "__main__":
    main()
