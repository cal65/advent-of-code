import pandas as pd
import numpy as np
from itertools import combinations, accumulate
from functools import reduce

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
