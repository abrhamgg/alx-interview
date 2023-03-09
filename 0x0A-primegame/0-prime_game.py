#!/usr/bin/python3
"""prime number module"""


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def generate_primes(n):
    """generate prime numbers up to n"""
    primes = []
    i = 2
    while i < n + 1:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes


def play_game(i, primes):
    """return 1 if ben wins or 2 if maria wins"""
    count = 0
    if i == 1:
        return 1
    if i == 2:
        return 2
    for p in primes:
        if i >= p:
            count += 1
    if count % 2 != 0:
        return 2
    else:
        return 1


def isWinner(x, nums):
    """main function"""
    if not nums or x < 1:
        return None
    num = max(nums)
    primes = generate_primes(num)
    Maria = 0
    Ben = 0
    for i in nums:
        result = play_game(i, primes)
        if result == 1:
            Ben += 1
        if result == 2:
            Maria += 1
    if Ben == Maria:
        return None
    else:
        if Ben > Maria:
            return 'Ben'
        return 'Maria'
