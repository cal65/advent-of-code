import pandas as pd

def solve_day1(file_path):
	num = pd.read_table(file_path, header=None)
	vec = list(num[0].values)
	increased = increase(vec[1:], vec[0])
	print(increased)
	triplets = create_triplet_sum(vec)
	return increase(triplets[1:], triplets[0])

def increase(vec, start):
	value = int(vec[0] > start)
	if len(vec) == 1:
		return value
	else:
		return value + increase(vec[1:], vec[0])

def create_triplet_sum(vec):
	if len(vec) == 3:
		return [sum(vec)]
	else:
		return [sum(vec[0:3])] + create_triplet_sum(vec[1:])