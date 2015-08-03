#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a file with several lines of text, each containing multiple words, as
input. Return the second-to-last word of each line. Assumes there are no empty
lines.
"""

from sys import argv

script, filename = argv

def penultimate_word(filename):
    with open(filename, "r") as input:
        for line in input.readlines():
            words = line.split()
            print(str(words[-2]))

if __name__ == "__main__":
    penultimate_word(filename)
