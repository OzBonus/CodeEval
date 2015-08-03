#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes as input a text file with a positive whole integer on each line.
Returns a 1 for each integer if it is a happy number, and a zero if it
is not a happy number.
"""

import sys

with open(sys.argv[1], "r") as f:
    NUMBERS = [line.strip() for line in f]

def happy_dance(number):
    "Returns the sum of the digits in number."
    return sum(int(digit) ** 2 for digit in str(number))

def happy_check(number):
    if number == 1:
        print(1)
    elif number == 4:
        print(0)
    else:
        return happy_check(happy_dance(number))

for number in NUMBERS:
    happy_check(number)
