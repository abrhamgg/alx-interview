#!/usr/bin/python3
"""nqueens"""
import sys


def is_safe(solution, pos):
    """Function to check if a queen can be placed
    at a given position"""
    for q in solution:
        if q[1] == pos[1]:
            return False
        if (q[0] + q[1]) == (pos[0] + pos[1]):
            return False
        if (q[0] - q[1]) == (pos[0] - pos[1]):
            return False
    return True


def queens(row, n, solution):
    """function that finds solution recursively
    in every row"""
    if row == n:
        print(solution)
    else:
        for col in range(n):
            pos = [row, col]
            if is_safe(solution, pos):
                solution.append(pos)
                queens(row + 1, n, solution)
                solution.remove(pos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solution = []
    queens(0, n, solution)
