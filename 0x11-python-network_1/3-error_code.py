#!/usr/bin/python3
"""Send request and display body
"""

import urllib.request
import urllib.error
import sys


try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        body = response.read().decode("utf-8")
        print(f"{body}")

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")


def main():
    """Empty function"""
    ...


if __name__ == "__main__":
    main()
