#!/usr/bin/python3
"""making change"""


def max_idx(my_list=[]):
    """return the max value from list and its index"""
    m = 0
    val = []
    for i in range(len(my_list)):
        if my_list[i] > m:
            val = [my_list[i], i]
    return val


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total."""
    my_total = 0
    ln = len(coins)
    num_coin = 0
    temp = total
    if total <= 0:
        return 0
    for i in range(ln):
        max_val = max_idx(coins)
        if max_val[0] > total:
            coins.pop(max_val[1])
        else:
            num_coin += total // max_val[0]
            unit = total // max_val[0]
            rem = total % max_val[0]
            my_total += coins[max_val[1]] * unit
            coins.pop(max_val[1])
            if my_total == temp:
                return num_coin
            total = rem
    return -1
