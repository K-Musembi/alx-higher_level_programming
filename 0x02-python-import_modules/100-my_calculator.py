#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print(r'Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = ['+', '-', '*', '/']
    if argv[2] == '+':
        print(f'{a} + {b} = {add(a, b)}')
    elif argv[2] == '-':
        print(f'{a} - {b} = {sub(a, b)}')
    elif argv[2] == '*':
        print(f'{a} * {b} = {mul(a, b)}')
    elif argv[2] == '/':
        print(f'{a} / {b} = {div(a, b)}')
    elif argv[2] not in operator:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
