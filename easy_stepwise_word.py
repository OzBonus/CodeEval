#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"


"""
Stepwise word

Challenge Description:

Print the longest word in a stepwise manner.

Input sample:

The first argument is a path to a file. Each line contains a test case
with a list of words that have different or the same length.

For example:

cat dog hello
stop football play
music is my life

Output sample:

Find the longest word in each line and print it in one line in a
stepwise manner. Separate each new step with a space. If there are
several words of the same length and they are the longest, then print
the first word from the list.

h *e **l ***l ****o
f *o **o ***t ****b *****a ******l *******l
m *u **s ***i ****c

Constraints:

1. The word length is from 1 to 10 characters.
2. The number of words in a line is from 5 to 15.
3. If there are several words of the same length and they are the
   longest, then print the first word from the list.
4. The number of test cases is 40.

"""

import sys

with open(sys.argv[1], "r") as cases:
    for line in cases:
        word = max(line.split(), key=len)
        index = 0
        for letter in word:
            print("*" * index + letter, end=" ")
            index += 1
        print()
