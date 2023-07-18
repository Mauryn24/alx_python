#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive")
    #print(f'{number} is positive')
elif number == 0:
    print(number, "is zero")
    #print(f'{number} is zero')
elif number < 0:
    print(number, "is negative")
    #print(f'{number} is negative')