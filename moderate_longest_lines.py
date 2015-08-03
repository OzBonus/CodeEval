#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file with several lines. The first line is a positive integer which
tells how many of the following lines to print. The printed lines must the
longest in the document and must be printed in order from longest to shortest.
"""

from sys import argv

script, filename = argv

def longest_lines(filename):
    lines    = []
    to_print = None
    with open(filename, "r") as input:
        for line in input.readlines():
            lines.append(line)
    to_print = int(lines.pop(0))
    lines.sort(key=len)
    for line in range(to_print):
        print(lines.pop(), end="")

if __name__ == "__main__":
    longest_lines(filename)
