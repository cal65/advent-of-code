from utils import *
import numpy as np
from functools import reduce


test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
expected_answer = 1227775554
expected_answer_b = 4174379265

def solve(input):
    series = input.split(',')
    invalid_ids = []
    ranges = [return_range(serie) for serie in series]
    for vals in ranges:
        invalid_ids += [val for val in vals if is_invalid(val)]
    total = sum(invalid_ids)
    return total

def solve_b(input):
    series = input.split(',')
    invalid_ids = []
    ranges = [return_range(serie) for serie in series]
    for vals in ranges:
        invalid_ids += [val for val in vals if is_invalid_b(val)]
    total = sum(invalid_ids)
    return total


def return_range(val):
    min, max = val.split('-')
    min = int(min)
    max = int(max)
    return list(np.arange(min, max+1))


def is_invalid(val):
    val_str = str(val)
    val_len = len(val_str)
    half = int(val_len / 2)
    return val_str[:half] == val_str[half:]

def is_invalid_b(val):
    val_str = str(val)
    val_len = len(val_str)
    facts = factors(val_len)
    for factor in facts:
        splits = split_str_by_value(val_str, factor)
        if list_all_equal(splits):
            return True
    return False

def split_str_by_value(string, value):
    if len(string) == 0:
        return []
    return [string[:value]] + split_str_by_value(string[value:], value)

def list_all_equal(string_list):
    return len(set(string_list)) == 1

def factors(n):
    return [i for i in range(1, int(n/2) + 1) if n % i == 0]

def test_part_a(input, expected_answer):

    return solve(input) == expected_answer

def test_part_b(input, expected_answer):
    return True


if __name__ == "__main__":
    input_data = read_input("day2.txt")
    print(test_part_a(test_data, expected_answer))

    print(test_part_b(test_data, expected_answer_b))
    answer = solve(input_data)
    print(answer)
    answer_b = solve_b(input_data)
    print(answer_b)
