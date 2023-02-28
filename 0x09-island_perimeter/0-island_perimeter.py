#!/usr/bin/python3
"""island perimeter"""


def island_perimeter(grid):
    """:return the perimeter of island"""
    width = 0
    height = 0
    count = 0
    for i in range(len(grid)):
        count = 0
        for j in range(len(grid)):
            if grid[i][j] == 1:
                count += 1
        if count > width:
            width = count
    
    for i in range(len(grid)):
        count = 0
        for j in range(len(grid)):
            if grid[j][i] == 1:
                count += 1
        if count > height:
            height = count
    
    return (width + height) * 2
