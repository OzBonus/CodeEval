#!/usr/bin/env python3
__author__ = "Christopher Perry"
__email__ = "ozbonus@gmail.com"

"""
Returns the largest prime palindrome less than 1,000.
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

def prime_palindrome(n):
    candidate = 3
    palindromes = [2]
    while candidate < n:
        if is_prime(candidate) and str(candidate) == str(candidate)[::-1]:
            palindromes.append(candidate)
        candidate += 2
    print(max(palindromes))

if __name__ == "__main__":
    prime_palindrome(1000)
