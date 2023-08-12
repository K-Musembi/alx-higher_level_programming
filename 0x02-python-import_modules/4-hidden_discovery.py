#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    lst = dir(hidden_4)

    for i in lst:
        if i[0] == '_':
            continue
        print(i)
