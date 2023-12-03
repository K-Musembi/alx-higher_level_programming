#!/usr/bin/python3
""" Display value of request id
"""

import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])

with urllib.request.urlopen(req) as response:
    x_id = response.getheader("X-Request-Id")

if x_id:
    print(f"{x_id}")


def main():
    """ Empty function """
    ...


if __name__ == "__main__":
    main()
