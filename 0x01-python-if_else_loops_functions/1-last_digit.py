#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_num = number * -1
    rem = (new_num % 10) * -1
else:
    rem = number % 10
print(f'Last digit of {number} is {rem}', end="")
if rem > 5:
    print(f' and is greater than {5}')
elif rem == 0:
    print(f' and is {0}')
elif rem < 6 and rem != 0:
    print(f' and is less than 6 and not 0')
