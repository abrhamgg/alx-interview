#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """function that returns pascal triangle
    :param n: number of rows
    :return: pascal numbers
    """
    new = [[]]
    p = []
    if n <= 0:
        return []
    if n == 1:
        p.append(1)
        new[0] = p
        return new
    for i in range(0, n):
        pa = []
        for j in range(0, i + 1):
            if i == 0 and j == 0:
                pa.append(1)
                continue
            if j == 0:
                pa.append(1)
            else:
                try:
                    pa.append(new[i][j - 1] + new[i][j])
                except IndexError:
                    pa.append(new[i][j - 1] + 0)
        new.append(pa)
    new.pop(0)
    return new
