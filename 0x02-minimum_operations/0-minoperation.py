#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste.Given a number n, write a method that
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    if n == 1:
        return 0
    operation = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operation += factor
            n // factor
        factor += 1
    return operation
