import pandas as pd
import numpy as np
import argparse
from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


def read_file(file_path):
    num = pd.read_table(file_path, header=None, dtype=str)
    return list(num[0].values)


def parse_number(number, position):
    return number[position]


def parse_list(binary_list, position):
    numbers = [parse_number(x, position) for x in binary_list]
    return numbers


def binary_mode(numbers, type):
    if type not in ["most", "least"]:
        raise ValueError("type must be either 'most' or 'least'")
    uniques = set()
    counts = {}
    for n in numbers:
        if n not in uniques:
            uniques.add(n)
            counts[n] = 1
        else:
            counts[n] += 1
    if type == "most":
        rate = max(counts, key=counts.get)
    elif type == "least":
        rate = min(counts, key=counts.get)
    return rate


def calculate_gamma_epsilon(binary_list):
    num_positions = len(binary_list[0])
    most = []
    least = []
    for i in range(0, num_positions):
        numbers = parse_list(binary_list, i)
        most.append(binary_mode(numbers, "most"))
        least.append(binary_mode(numbers, "least"))
    return_dict = {"gamma": binaryToDecimal(most), "epsilon": binaryToDecimal(least)}
    return return_dict


def binaryToDecimal(binary):
    """
    binary is a string of 0s and 1s
    """
    value = 0
    n = len(binary)
    for i in range(0, n):
        value += int(binary[n - i - 1]) * 2 ** i
    return value


def test_calculate_gamma():
    b_list = ["1100", "1100", "1101", "1010"]
    return calculate_gamma(b_list)

if __name__ == "__main__":
    """
    Usage: python append_to_export.py filepath.csv --username [--update] [wait]
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    file_path = args.file_path
    text = read_file(file_path)
    rates = calculate_gamma_epsilon(text)
    print(rates['gamma'] * rates['epsilon'])
