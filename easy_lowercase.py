#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file with several lines of text using a mix of uppercase and lowercase letters. Returns those lines in only lowercase. Assumes there are no empty lines.
"""

from sys import argv

script, filename = argv

def lowercase(filename):
    with open(filename, "r") as input:
        for line in input.readlines():
            print(line.lower()[:-1])

if __name__ == "__main__":
    lowercase(filename)
