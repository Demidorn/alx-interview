#!/usr/bin/python3

"""Island Perimeter"""


def island_perimeter(grid):
    """a function that that returns the perimeter
    of the island described in grid
    """
    if not grid or not grid[0]:
        return 0

    def is_water_or_out_of_bounds(x, y):
        '''Check if the cell is water or out of bounds'''
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return True
        return grid[x][y] == 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                '''Check all four directions'''
                if is_water_or_out_of_bounds(i - 1, j):
                    perimeter += 1
                if is_water_or_out_of_bounds(i + 1, j):
                    perimeter += 1
                if is_water_or_out_of_bounds(i, j - 1):
                    perimeter += 1
                if is_water_or_out_of_bounds(i, j + 1):
                    perimeter += 1

    return perimeter
