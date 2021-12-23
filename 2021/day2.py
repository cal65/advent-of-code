import pandas as pd
import numpy as np
import argparse

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

if __name__ == "__main__":
    """
    Usage: python append_to_export.py filepath.csv --username [--update] [wait]
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    file_path = args.file_path
    text = read_file(file_path)
    x, y = analyze_position(text, 0, 0)
    print(x * y)