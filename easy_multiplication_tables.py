#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Print out a multiplication table covering from 1x1 to 12x12. Numbers are
formatted so that they are right-aligned on cells of width four. The first three
rows should look like this:
   1   2   3   4   5   6   7   8   9  10  11  12
   2   4   6   8  10  12  14  16  18  20  22  24
   3   6   9  12  15  18  21  24  27  30  33  36
"""

for r in range(1, 13):
    for c in range(1, 13):
        print("{:>4}".format(c*r), end="")
    print() # Just need this for the line break.
