#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if num >= 97 and num <= 122:
            num -= 32
        if i == str[-1]:
            print(chr(num))
        else:
            print(chr(num), end="")
