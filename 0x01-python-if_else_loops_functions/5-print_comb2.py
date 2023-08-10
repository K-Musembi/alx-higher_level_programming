#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print(str(i).zfill(2), end=", ")
    elif i == 99:
        print(f'{i}')
    else:
        print(f'{i}', end=", ")
