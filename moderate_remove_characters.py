#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file where each line is in the format "x, y" where x is a string of
words and y is a set of characters. Returns the string of words in x after first
removing the letters in y.
"""

from sys import argv
import re

script, filename = argv

def moderate_remove_characters(filename):
    with open(filename, "r") as input:
        for line in input.readlines():
            words, chars = line.split(",")
            chars = chars.replace(" ", "")
            print(re.sub(str("["+chars+"]"), "", words))

if __name__ == "__main__":
    moderate_remove_characters(filename)
