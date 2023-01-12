#!/usr/bin/python3

"""minimum operation"""
import math


def minOperations(n):
    """In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that
    calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""

    factor = 0
    if n <= 1:
        return 0
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            factor += 1

    if factor == 0:
        return n
    op = math.log(n, 2)
    if (n % op == 0):
        return int(op) * 2
    if int(op) >= 1:
        return (int(op) * 2) + round(op - 2)
