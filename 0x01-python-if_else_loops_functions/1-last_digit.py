#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
string = (f"Last digit of {number} is {last_digit}")
if last_digit > 5:
    print(f"{string} and greater than 5")
elif last_digit == 0:
    print(f"{string} and is 0")
elif last_digit < 6 and not 0:
    print(f"{string} and is less than 6 and not 0")