#!/usr/bin/python3
"""prime game"""


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def play_game(n):
    "return 1 if ben wins else return 2 if maria wins"
    if n == 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        if isPrime(i):
            count += 1
    if count % 2 == 0:
        return 1
    else:
        return 2


def isWinner(x, nums):
    """determines the winner of the game"""
    players = {
        'Maria': 0,
        'Ben': 0
    }
    if nums == [] or x <= 0:
        return None
    for i in nums:
        result = play_game(i)
        if result == 1:
            players['Ben'] += 1
        elif result == 2:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None
