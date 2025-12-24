from utils import *
import numpy as np
from typing import List

test_data = []
expected_answer = None
expected_answer_b = None

def solve(input_data):
    return

def solve_part_b(input_data):
    return

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
