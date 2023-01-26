#!/usr/bin/python3
"""valid utf8"""


def validUTF8(data):
    """method that determines if a given data set represents a
    valid UTF-8 encoding"""
    if data:
        for d in data:
            if d is int and len(bin(d)) > 10:
                return False
            if d is str and len(d) > 8:
                return False
    return True
