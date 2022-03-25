import pandas as pd
import numpy as np
import argparse
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)


def read_file(file_path):
	num = pd.read_table(file_path, header=None)
	return list(num[0].values)

def split_text(text, character = ' '):
	parts = text.split(character)
	return parts

def analyze_movement(direction, distance, x, y):
	if direction == 'up':
		y -= distance
	elif direction == 'down':
		y += distance
	elif direction == 'forward':
		x += distance
	return x, y


def analyze_position(text, x, y):
	parts = split_text(text[0], ' ')
	x, y = analyze_movement(parts[0], int(parts[1]), x, y)
	if len(text) == 1:
		return x, y
	else:
		x, y = analyze_position(text[1:], x, y)
		return x, y

def analyze_aim(direction, distance, x, y, aim):
	if direction == 'up':
		aim -= distance
	elif direction == 'down':
		aim += distance
	elif direction == 'forward':
		x += distance
		y += distance * aim
	return x, y, aim

#@lru_cache()
def analyze_position_aim(text, x, y, aim):
	parts = split_text(text[0], ' ')
	x, y, aim = analyze_aim(parts[0], int(parts[1]), x, y, aim)
	if len(text) == 1:
		return x, y, aim
	else:
		x, y, aim = analyze_position_aim(text[1:], x, y, aim)
		return x, y, aim

if __name__ == "__main__":
    """
    Usage: python append_to_export.py filepath.csv --username [--update] [wait]
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    file_path = args.file_path
    text = read_file(file_path)
    x, y, aim = analyze_position_aim(text, 0, 0, 0)
    print(x * y)