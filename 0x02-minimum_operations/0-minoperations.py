#!/usr/bin/python3

"""minimum operation"""
import math


def minOperations(n):
    """In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that
    calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""

    if n < 2 or not isinstance(n, int):
        return 0
    count = 1
    final = []
    while n != 1:
        count += 1
        if n % count == 0:
            while (n % count == 0 and n != 1):
                n /= count
                final.append(count)
    return sum(final)
