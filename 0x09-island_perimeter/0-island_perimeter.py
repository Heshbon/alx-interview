#!/usr/bin/python3
""" The island function parameter"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    # Calculate the perimeter of the island described in grid
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for a in range(rows):
        for b in range(cols):
            if grid[a][b] == 1:
                perimeter += 4
                if b < cols - 1 and grid[a][b + 1] == 1:
                    perimeter -= 2
                if a < rows - 1 and grid[a + 1][b] == 1:
                    perimeter -= 2

    return perimeter
