#!/usr/bin/python3
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f'{0} arguments.')
    elif len(sys.argv) == 2:
        print(f'{1} argument:')
        print(f'{1}: ' + sys.argv[1])
    else:
        args = len(sys.argv) - 1
        print(f'{args} arguments:')
        for i in range(1, len(sys.argv)):
            print(f'{i}: ' + sys.argv[i])
