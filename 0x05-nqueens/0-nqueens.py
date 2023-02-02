#!/usr/bin/python3
"""nqueens"""
import sys

result = []


def is_pos_safe(board, row, col):
    """function to check if position is safe
    place a queen"""

    '# check rows on left'
    for i in range(col):
        if board[row][i]:
            return False

    '# check upper diagonal on the left'
    y = row
    x = col
    while y >= 0 and x >= 0:
        if board[y][x]:
            return False
        y -= 1
        x -= 1

    y = row
    x = col
    while x >= 0 and y < 4:
        if(board[y][x]):
            return False
        y = y + 1
        x = x - 1
    return True


def n_queens(board, col, size):
    """n queens"""
    if col == size:
        v = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    new = [i, j]
                    v.append(new)
        if v not in result:
            result.append(v)
        return True

    res = False

    for i in range(size):
        if is_pos_safe(board, i, col):
            board[i][col] = 1

            res = n_queens(board, col + 1, size) or res
            board[i][col] = 0
    return res


def solveNQ(n):
    result.clear()
    board = [[0 for j in range(n)]
             for i in range(n)]
    n_queens(board, 0, n)
    return result


memory = []
n = 0
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

res = solveNQ(n)
'''first = res[0]
memory.append(first[0])
print(first)'''
for i in res:
    if i[0] not in memory:
        print(i)
        '''memory.append(i[0])'''
