#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file with an integer on each line. Returns the sum of the digits in
each integer. Assumes there are no blank lines.
"""

from sys import argv

script, filename = argv

def sum_of_digits(filename):
    with open(filename, "r") as input:
        for line in input.readlines():
            line = int(line)
            print(sum(int(digit) for digit in str(line)))

if __name__ == "__main__":
    sum_of_digits(filename)
