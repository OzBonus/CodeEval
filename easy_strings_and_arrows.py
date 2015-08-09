#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"


"""
Strings and arrows

Challenge Description:

You have a string composed of the following symbols: '>', '<', and '-'.
Your task is to find, count, and print to the output a number of arrows
in the string. An arrow is a set of the following symbols: '>>-->' or
'<--<<'.  Note that one character may belong to two arrows at the same
time. Such example is shown in the line #1.  Input sample:

The first argument is a path to a file. Each line includes a test case
with a string of different length from 10 to 250 characters. The string
consists of '>', '<', and '-' symbols.

For example:

<--<<--<<
<<>>--><--<<--<<>>>--><
<-->>

Output sample:

Print the total number of found arrows for each test case.

For example:

2
4
0

Constraints:

1. An arrow is a set of the following symbols: '>>-->' or '<--<<'.
2. One symbol may belong to two arrows at the same time.
3. The number of test cases is 40.
"""

import sys

with open(sys.argv[1], "r") as cases:
    for case in cases.readlines():
        arrow_a = ">>-->"
        arrow_b = "<--<<"
        string  = case
        matches = 0
        while len(string) >= 5:
            if arrow_a in string[0:5] or arrow_b in string[0:5]:
                matches += 1
            string = string[1:]
        print(matches)
