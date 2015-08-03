#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Reads a file with lines consisting of space-delimited integers labeled x y z.
Produces a range of numbers for each line of length z and replace all numbers
that are divisible only by x with "F", divisible only by y with "B", and
divisible by both with "FB".
"""

from sys import argv

script, filename = argv

def fizz_buzz(filename):
    with open(filename, "r") as input:
        for line in input.readlines():
            x, y, z = line.split()
            numbers = [n for n in range(1, int(z)+1)]
            for i, n in enumerate(numbers):
                if n % int(x) == 0 and n % int(y) == 0:
                    numbers[i] = "FB"
                elif n % int(x) == 0:
                    numbers[i] = "F"
                elif n % int(y) == 0:
                    numbers[i] = "B"
            print(" ".join(map(str, numbers)))

if __name__ == "__main__":
    fizz_buzz(filename)
