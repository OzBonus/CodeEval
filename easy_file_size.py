#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Returns the size, in bytes, of a file.
"""

from sys import argv
import os

script, filename = argv

def size_bytes(filename):
    print(os.path.getsize(filename))

if __name__ == "__main__":
    size_bytes(filename)
