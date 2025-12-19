from utils import *
import numpy as np
from typing import List

test_data = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
expected_answer = 357
expected_answer_b = 3121910778619

def solve(input):
    answer = 0
    for val in input:
        code = str(val)
        answer += parse_battery(code)
    return answer

def parse_battery(code: str):
    first, second = largest_first_and_second(0, 0, code)
    return 10 * first + second

def largest_first_and_second(first, second, code: str):
    if len(code) == 0:
        return first, second
    # evaluate first letter
    c_int = int(code[0])

    if c_int > first:
        # not last value
        if len(code) > 1:
            first = c_int
            second = 0
        else:
            second = c_int
    elif c_int > second:
        second = c_int
    return largest_first_and_second(first, second, code[1:])

def largest_n(code_list: List[int], i, n=12):
    if len(code_list) == n:
        return code_list
    if (i+1) >= len(code_list):
        return code_list[:n]
    if code_list[i] < code_list[i+1]:
        code_list.pop(i)
        i = max(0, i-1) # look backwards and compare again
    else:
        i += 1
    return largest_n(code_list, i, n)

def int_to_list(number):
    number_str = str(number)
    return [int(s) for s in number_str]

def list_to_int(num_list):
    return int("".join(map(str, num_list)))

def flow_b(val):
    code_list = int_to_list(val)
    longest_list = largest_n(code_list, i=0, n=12)
    return list_to_int(longest_list)

def solve_part_b(input_data):
    answer = 0
    for val in input_data:
        answer += flow_b(val)
    return answer

def test_part_a(input_data, expected_answer):
    return solve(input_data) == expected_answer

def test_part_b(input_data, expected_answer):
    return solve_part_b(input_data) == expected_answer


if __name__ == "__main__":
    input_data = read_lines("day3.txt")
    print(test_part_a(test_data, expected_answer))
    answer = solve(input_data)
    print(answer)
    print("**Part B**")
    print(test_part_b(test_data, expected_answer_b))
    print(solve_part_b(test_data))
    answer_part_b = solve_part_b(input_data)
    print(answer_part_b)
