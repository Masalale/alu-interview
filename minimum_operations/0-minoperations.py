#!/usr/bin/python3
"""
0-minoperations module

This module contains a single function `minOperations(n)` that calculates
the minimum number of operations (Copy All and Paste) required to reach
exactly n 'H' characters in a text editor starting with one 'H'.
"""


def minOperations(n):
    if n < 2:
        return 0
    ops = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1
    return ops