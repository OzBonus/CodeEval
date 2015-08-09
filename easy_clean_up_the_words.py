#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"


"""
Clean up the words

Challenge Description:

You have a list of words. Letters of these words are mixed with extra
symbols, so it is hard to define the beginning and end of each word.
Write a program that will clean up the words from extra numbers and
symbols.

Input sample:

The first argument is a path to a file. Each line includes a test case with a list of words: letters are both lowercase and uppercase, and are mixed with extra symbols.

For example:

(--9Hello----World...--)
Can 0$9 ---you~
13What213are;11you-123+138doing7

Output sample:

Print the cleaned up words separated by spaces in lowercase letters.

For example:

hello world
can you
what are you doing

Constraints:

1. Print the words separated by spaces in lowercase letters.
2. The length of a test case together with extra symbols can be in a
   range from 10 to 100 symbols.
3. The number of test cases is 40.

"""

import sys
import re

with open(sys.argv[1], "r") as cases:
    for line in cases:
        string = re.split("[^a-zA-Z]*", line)
        string[:] = [item.lower() for item in string if item != ""]
        print(" ".join(string))
