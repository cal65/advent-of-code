from day2 import read_file
import math
import numpy as np

def parse_file(d9):
    parsed_arr = [x.split(' ') for x in d9]
    parsed_arr = [[int(x) for x in p] for p in parsed_arr]
    return parsed_arr
        

def iterate_diffs(arr):
    n = 0
    diffs  = np.diff(arr)
    last_diff = [diffs[-1]]
    while not all([d == 0 for d in diffs]):
        diffs = np.diff(diffs)
        last_diff.append(diffs[-1])
        n += 1

    next_num = sum(last_diff)
    return next_num

def iterate_diffs_part2(arr):
    diffs  = np.diff(arr)
    diffs_array = [arr, diffs]
    while not all([d == 0 for d in diffs]):
        diffs = np.diff(diffs)
        diffs_array.append(diffs)
    n = len(diffs_array)
    for i in range(1, n):
        prepend = diffs_array[-i-1][0] - diffs_array[-i][0]
        diffs_array[-i-1] = np.insert(diffs_array[-i-1], 0, prepend)
    return diffs_array[0][0]


if __name__ == "__main__":
    d9 = read_file("day9.txt")
    parsed_arr = parse_file(d9)
    test_arr = [10,  13,  16,  21,  30,  45]
    print(iterate_diffs(test_arr))

    next_nums = [p[-1] + iterate_diffs(p) for p in parsed_arr]
    answer = np.sum(next_nums)
    print(answer)
    prepends_part2 = [iterate_diffs_part2(p) for p in parsed_arr]
    answer_part2 = sum(prepends_part2)
    print(answer_part2)