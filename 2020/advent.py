import pandas as pd
import numpy as np
from itertools import combinations, accumulate
from functools import reduce
import operator
import re

def day1(file, n):
	 d1 = pd.read_table(file, header=None)[0]
	 pairs = combinations(d1, n)

	 def inner_arith(x: tuple, target_sum):
	 	if sum(x) == target_sum:
	 		return reduce((lambda x, y: x * y), x)
	 	else:
	 		return 0
	 val = 0	
	 for pair in pairs:
	 	val += inner_arith(pair, 2020)
	 return val


def read_df(file):
	d2 = pd.read_table(file, header=None)[0]
	split_tuples = list(d2.str.split(': '))
	password_df = pd.DataFrame.from_records(split_tuples, columns = ['policy', 'password'])
	return password_df

def transform_df(df, col):
	split_df = df[col].str.split(' |-').apply(pd.Series) 
	split_df.columns = ['min', 'max', 'letter']
	split_df['min'] = split_df['min'].astype(int)
	split_df['max'] = split_df['max'].astype(int)
	df = pd.concat([df, split_df], axis=1)
	return df

def day2(file):
	password_df = read_df(file)
	password_df = transform_df(password_df, 'policy')
	password_df['count'] = password_df.apply(lambda x: x.password.count(x.letter), axis=1)
	password_df['pass'] = (password_df['count'] >= password_df['min']) & (password_df['count'] <= password_df['max'])

	return password_df['pass'].sum()

def day2b(file):
	password_df = read_df(file)
	password_df = transform_df(password_df, 'policy')
	password_df['position_1'] = password_df.apply(lambda x: x.password[x['min']-1] == x.letter, axis = 1) 
	password_df['position_2'] = password_df.apply(lambda x: x.password[x['max']-1] == x.letter, axis = 1) 
	password_df['pass'] = (password_df['position_1']) != (password_df['position_2']) 
	return password_df['pass'].sum()

def day3(file):
	tree_grid = pd.read_table(file, header=None)[0]
	rows = []
	for row in tree_grid:
		rows.append(list(row*300))
	grid = np.matrix(rows)
	return grid

#recursive solution
def traverse(grid, start_row, start_col, x, y, tree_char = "#"):
	grid_row, grid_col = grid.shape
	if (start_row + y > grid_row) | (start_col + x > grid_col):
		return 0
	else:
		value = 1 if grid[start_row, start_col] == tree_char else 0
		return value + traverse(grid, start_row + y, start_col + x, x, y, tree_char = tree_char)


def traverse_part_two(grid):
	slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
	options = []
	for slope in slopes:
		options.append(traverse(grid, 0, 0, slope[0], slope[1]))
	return reduce(operator.mul, options)

def day4(file):
	 d4 = pd.read_table(file, header=None, skip_blank_lines=False)[0]
	 return d4

def parse_passport(l):
	passport_list = []
	passport = {}
	for line in l:
		if pd.isnull(line):
			passport_list.append(passport)
			passport = {}
		else:
			line_split = line.split(' ')
			for split in line_split:
				pair = split.split(':')
				passport[pair[0]] = pair[1]
	# this isn't ideal, but because we aren't parsing the last NA, the final loop is not appended
	passport_list.append(passport)
	return passport_list

def check_passport(passport, required_fields):
	return all(x in passport.keys() for x in required_fields)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def count_valid_passports(file):
	passport_list = parse_passport(day4(file))
	return  sum([check_passport(passport, required_fields) for passport in passport_list])
	
def test_day4():
	assert(check_passport({'ecl':'gry', 'pid':'860033327', 'eyr':'2020', 'hcl':'#fffffd',
		'byr':'1937', 'iyr':'2017', 'cid':'147', 'hgt': '183cm'}, required_fields) == 1)
	assert(check_passport({'iyr':'2013', 'ecl':'amb', 'cid':'350', 'eyr':'2023', 'pid':'028048884',
		'hcl':'#cfa07d', 'byr':'1929'}, required_fields) == 0)
	assert(check_passport({'hcl':'#ae17e1', 'iyr':'2013',
		'eyr':'2024',
		'ecl':'brn', 'pid':'760753108', 'byr':'1931',
		'hgt':'179cm'}, required_fields) == 1)
	assert( check_passport({'hcl':'#cfa07d', 'eyr':'2025', 'pid':'166559648',
		'iyr':'2011', 'ecl':'brn', 'hgt':'59in'}, required_fields)== 0)

def check_valid_passports_b(file):
	passport_list = parse_passport(day4(file))
	valid_passports = [p for p in passport_list if check_passport(p, required_fields)]
	check_b = [check_passport_fields(x) for x in valid_passports]   
	return sum(check_b)

def check_passport_fields(passport):
	return all([_check_byr(passport),
		_check_eyr(passport),
		_check_iyr(passport),
	   	_check_hgt(passport),		
	   	_check_hcl(passport),
	   	_check_ecl(passport),
	   	_check_pid(passport)]) 

def _check_yr(passport, yr_field, low, high):
	try:
		yr = int(passport[yr_field])
	except:
		return False
	return (yr >= low) & (yr <= high)

def _check_byr(passport):
	return _check_yr(passport, 'byr', 1920, 2002)

def _check_iyr(passport):
	return _check_yr(passport, 'iyr', 2010, 2020)

def _check_eyr(passport):
	return _check_yr(passport, 'eyr', 2020, 2030)

def _check_hgt(passport):
	hgt_raw = passport['hgt']
	try:
		hgt = int(re.findall('[0-9]+', hgt_raw)[0])
	except:
		return False
	try:
		unit = re.findall('[a-z]+', hgt_raw)[0]
	except:
		return False
	if unit == 'cm':
		return (hgt >= 150) & (hgt <= 193)
	if unit == 'in':
		return (hgt >= 59) & (hgt <= 76)
	else:
		return False

def _check_hcl(passport):
	hcl = passport['hcl']
	return re.match('^\\#[a-z|0-9]{6}(?![0-9])', hcl) is not None

def _check_ecl(passport):
	ecl = passport['ecl']
	return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def _check_pid(passport):
	pid = passport['pid']
	return re.match('[0-9]{9}(?![0-9])', pid) is not None


def test_check_valid_passport():
	test_passport = {
	'pid':'087499704', 'hgt':'74in', 'ecl':'grn',
	'iyr':'2012', 'eyr':'2030', 'byr':'1980',
	'hcl':'#623a2f'
	}
	assert(check_passport_fields(test_passport) == True)
