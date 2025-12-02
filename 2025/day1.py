from utils import *
import numpy as np

test_data = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

def rotate(starting_point, rotate_str):
    dir = rotate_str[0]
    dir_map = {"L": -1, "R": 1}
    dir_int = dir_map.get(dir)
    rotate_int = int(rotate_str[1:])
    next_point = starting_point + dir_int * rotate_int
    return next_point % 100

def run_sequence(seq):
    starting_point = 50
    values = []
    for s in seq:
        starting_point = rotate(starting_point, s)
        values.append(starting_point)
    return values

def password_conversion(values):
    return len([v for v in values if v == 0])

def rotate_part_b(starting_point, rotate_str):
    dir = rotate_str[0]
    dir_map = {"L": -1, "R": 1}
    dir_int = dir_map.get(dir)
    rotate_int = int(rotate_str[1:])
    next_point = starting_point + dir_int * rotate_int
    rotations = abs(np.floor(next_point / 100))  #+ int(next_point == 0)
    if next_point < 0 and starting_point == 0:
        rotations -= 1
    elif next_point % 100 == 0 and next_point > 0:
        rotations -= 1
    return next_point % 100, int(rotations)

def run_sequence_part_b(seq):
    starting_point = 50
    values = []
    rotations_list = []
    for s in seq:
        starting_point, rotations = rotate_part_b(starting_point, s)
        values.append(starting_point)
        rotations_list.append(rotations)
    return values, rotations_list

def test_():
    nums = run_sequence(test_data)
    return password_conversion(nums) == 3

def test_part_b():
    values, rotations_list = run_sequence_part_b(test_data)
    return sum(rotations_list) + password_conversion(values) == 6



if __name__ == "__main__":
    print(test_())
    file_raw = read_input("day1.txt")
    input_data = file_raw.split("\n")
    nums = run_sequence(input_data)
    part1 = password_conversion(nums)
    print(part1)
    print(test_part_b())
    vals, nums_partb = run_sequence_part_b(input_data)
    print(sum(nums_partb) + part1)
