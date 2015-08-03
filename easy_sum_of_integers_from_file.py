#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file wherein each line is an integer and returns the sum of all
integers.
"""

import sys

def sum_of_integers_from_file(filename = sys.argv[1]):
    with open(filename, "r") as data:
        print(sum([int(n) for n in data.readlines()]))

if __name__ == "__main__":
    sum_of_integers_from_file()
