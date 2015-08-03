#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file wherein each line is a hexidecimal number and returns each
number as a decimal number. Assumes there are no empty lines.
"""

from sys import argv

script, filename = argv

def hex_to_decimal(filename):
    with open(filename, "r") as inputty:
        for line in inputty.readlines():
            print(int(line, 16))

if __name__ == "__main__":
    hex_to_decimal(filename)
