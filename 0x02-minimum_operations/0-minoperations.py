#!/usr/bin/python3

"""minimum operation"""
import math


def minOperations(n):
    """In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that
    calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""

    if n <= 1:
        return 0
    op = math.log(n, 2)
    if int(op) >= 1:
        return (int(op) * 2) + 1
    return int(op) * 2
