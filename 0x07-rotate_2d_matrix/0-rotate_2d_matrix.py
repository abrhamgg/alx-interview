#!/usr/bin/python3
"""rotate matrix"""


def rotate_2d_matrix(matrix):
    """rotate matrix 90 degrees clockwise"""
    changed = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and [j, i] not in changed:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                changed.append([i, j])
    for row in matrix:
        last_idx = len(row) - 1
        for i in range(len(row) // 2):
            row[i], row[last_idx] = row[last_idx], row[i]
            last_idx -= 1
