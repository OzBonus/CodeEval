#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Takes a text file wherein each line is a sentence and returns each sentence in
roller coaster case, such that the following sentence ...

To be, or not to be: that is the question.

... will be changed into ...

To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
"""

import sys

def roller_coaster(filename = sys.argv[1]):
    with open(filename, "r") as data:
        for line in data:
            string = ""
            up_this = True
            for char in line:
                if char.isalpha() and up_this:
                    string += char.upper()
                    up_this = not up_this
                elif char.isalpha():
                    string += char
                    up_this = not up_this
                else:
                    string += char
            print(string, end="")

if __name__ == "__main__":
    roller_coaster()
