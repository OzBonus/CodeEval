#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Take a text file wherein each line of text consist of space delimited characters
followed by an integer. This program prints the Mth element of the (1-based)
list. In the case of an index error, that input is ignored.
"""

import sys

def mth_to_last_element(filename = sys.argv[1]):
    with open(filename, "r") as data:
        for line in data:
            try:
                # Could do this in fewer lines, but this ain't code golf.
                chars = line.split()
                index = int(chars.pop())
                print(chars[-index])
            except IndexError:
                pass

if __name__ == "__main__":
    mth_to_last_element()
