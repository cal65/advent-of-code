import pandas as pd
import re

def solve_day1(file_path):
    num = pd.read_table(file_path, header=None)
    value = num[0].apply(parse_text).sum() 
    return value
	
def parse_text(text):
    m = re.findall('\d+', text)
    if len(m) > 1:
        int_strings = m[0][0], m[-1][-1]
    else:
        int_strings = m[0][0], m[0][-1]
    value = int(''.join(int_strings))
    return value

test_array = ['two1nine', 'eight2three', 'abc1two3xyz', 
              'x2one3four', '4nine8seven2', 'z1eight234', '7pqrstsixteen']

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dict_numbers = {n: i+1 for i, n in enumerate(numbers)} 

def parse_numbers_part2(text):
    nchar = len(text)
    for n in range(3, nchar):
        for num in numbers:
            if num in text[:n]:
                text = text.replace(num, str(dict_numbers[num]), 1)
                break
            else:
                continue
            break
        for num in numbers:
            if num in text[-n:]:
                text = text.replace(num, str(dict_numbers[num]), 1)
                break
            break    
    return text

def solve_day1_part2(array):
    array = array.apply(parse_numbers_part2)
    value = array.apply(parse_text).sum() 
    return value

