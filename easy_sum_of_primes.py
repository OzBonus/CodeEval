#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Finds the first 1,000 prime numbers and returns their sum.
"""

import math

def is_prime(candidate):
    """
    Assumes n is an odd number.
    """
    for integer in range(3, int(math.sqrt(candidate)) + 1, 2):
        if candidate % integer == 0:
            return False
    return True

def sum_of_primes(n):
    primes    = [2]
    candidate = 3
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 2
    print(sum(primes))

if __name__ == "__main__":
    sum_of_primes(1000)
