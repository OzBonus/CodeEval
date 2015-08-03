#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a file with a series of words on each line and returns those lines with
the words reversed. Empty lines, if any, are skipped.
"""

from sys import argv

script, filename = argv

def reverse_words(filename):
    with open(filename, "r") as input:
        for line in input.readlines():
            words = line.split()
            if not words:
                continue
            else:
                print(" ".join(words[::-1]))

if __name__ == "__main__":
    reverse_words(filename)
