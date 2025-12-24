from utils import *
import numpy as np
import pandas as pd
from typing import List

test_data = ["..@@.@@@@.", "@@@.@.@.@@", "@@@@@.@.@@", "@.@@@@..@.", "@@.@@@@.@@",
".@@@@@@@.@", ".@.@.@.@@@", "@.@@@.@@@@", ".@@@@@@@@.", "@.@.@@@.@."]
expected_answer = 13
expected_answer_b = 43

def solve(input_data):
    rolls_list = find_rolls(input_data)
    return len(rolls_list)

def find_coordinates(x, y, width, height):
    xs = [x + i for i in [-1, 0, 1] if (x+i) >= 0 and (x+i) < width]
    ys = [y + i for i in [-1, 0, 1] if (y+i) >= 0 and (y+i) < height]
    coords = [(x1, y1) for x1, y1 in zip(np.repeat(xs, len(ys)), ys * len(xs))]
    try:
        coords.remove((x, y))
    except:
        raise ValueError(f"invalid x {x}")
    return coords

def find_neighbors(grid, coords):
    neighbors = [grid[x1][y1] for x1, y1 in coords]
    return neighbors


def which_neighbors(neighbors, coords):
    return [c for n, c in zip(neighbors, coords) if n == "@"]

def find_rolls(grid):
    width = len(grid)
    height = len(grid[0])
    rolls_list = []
    for i in range(0, width):
        for j in range(0, height):
            if grid[i][j] == "@":
                coords = find_coordinates(i, j, width, height)
                neighbors = find_neighbors(grid, coords)
                rolls = which_neighbors(neighbors, coords)
                rolls_count = len(rolls)
                if rolls_count < 4:
                    rolls_list.append((i, j))
    return rolls_list

def find_rolls_b(grid):
    width = len(grid)
    height = len(grid[0])
    rolls_list = []
    new_grid = grid.copy()
    for i in range(0, width):
        for j in range(0, height):
            if grid[i][j] == "@":
                coords = find_coordinates(i, j, width, height)
                neighbors = find_neighbors(grid, coords)
                rolls = which_neighbors(neighbors, coords)
                rolls_count = len(rolls)
                if rolls_count < 4:
                    rolls_list.append((i, j))
                    # replace @ with . on that spot
                    new_grid[i] = replace_string_index(new_grid[i], index_to_replace=j)
    return rolls_list, new_grid

def solve_part_b(input_data):
    rolls_total = 0
    while True:
        rolls_list, grid_new = find_rolls_b(input_data)
        rolls_list_len = len(rolls_list)
        rolls_total += rolls_list_len
        if rolls_list_len == 0:
            break
        input_data = grid_new
    return rolls_total

def replace_string_index(original_string, index_to_replace):
    new_string = original_string[:index_to_replace] + "." + original_string[index_to_replace + 1:]
    return new_string

def test_part_a(input_data, expected_answer):
    return solve(input_data) == expected_answer

def test_part_b(input_data, expected_answer):
    return solve_part_b(input_data) == expected_answer


if __name__ == "__main__":
    input_data = read_lines("day4.txt")
    print(test_part_a(test_data, expected_answer))
    answer = solve(input_data)
    print(answer)
    print("**Part B**")
    print(test_part_b(test_data, expected_answer_b))
    print(solve_part_b(test_data))
    answer_part_b = solve_part_b(input_data)
    print(answer_part_b)
