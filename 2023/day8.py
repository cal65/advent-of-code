from day2 import read_file
import math


test1 = ['RL',
'AAA = (BBB, CCC)',
'BBB = (DDD, EEE)',
'CCC = (ZZZ, GGG)',
"DDD = (DDD, DDD)",
"EEE = (EEE, EEE)",
"GGG = (GGG, GGG)",
"ZZZ = (ZZZ, ZZZ)"]


test2 = ['LLR',
'AAA = (BBB, BBB)',
'BBB = (AAA, ZZZ)',
'ZZZ = (ZZZ, ZZZ)']

def parse_instructions(text):
    instructions = list(text[0]) # turn the string into a list of characters
    coords = text[1:]
    coords_raw = [c.split(' = ') for c in coords]
    coords_dict = {}
    for c in coords_raw:
        coords_dict[c[0]] = c[1].replace('(', '').replace(')', '').split(', ')
    return instructions, coords_dict


def navigate(instructions, coords_dict, start='AAA'):
    coord = start
    instructions_map = {'L': 0, 'R': 1}
    steps = 0
    while coord != 'ZZZ':
        for instr in instructions:
            d = instructions_map[instr]
            coord = coords_dict[coord][d]
            steps += 1
    return steps


def navigate_p2_single(instructions, coords_dict, start='AAA'):
    coord = start
    instructions_map = {'L': 0, 'R': 1}
    steps = 0
    while not end_with_z(coord):
        for instr in instructions:
            d = instructions_map[instr]
            coord = coords_dict[coord][d]
            steps += 1
    return steps


def lcm(a, b):
    # Helper function to calculate LCM of two numbers
    return abs(a * b) // math.gcd(a, b)

def lcm_array(arr):
    # Calculate the LCM of an array of numbers
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result


def navigate_part2(instructions, coords_dict, verbose=False):
    coords = [c for c in coords_dict.keys() if c[-1] == 'A']
    # while True:
    #     for instr in instructions:
    #         d = instructions_map[instr]
    #         coords = [coords_dict[c][d] for c in coords]
    #         steps += 1
    #         if verbose:
    #             print(coords)
    #         if all([end_with_z(c) for c in coords]):
    #             return steps
    #         if steps % 100000 == 0:
    #             print(steps)
    # discarding this approach, near infinite loop
    # instead we will go one at a time and then find the lcm
    steps = [navigate_p2_single(instructions, coords_dict, start=c) for c in coords]
    steps_all = lcm_array(steps)
    return steps_all


def end_with_z(t):
    return list(t)[-1] == 'Z'

test3=['LR',
'11A = (11B, XXX)',
'11B = (XXX, 11Z)',
'11Z = (11B, XXX)',
'22A = (22B, XXX)',
'22B = (22C, 22C)',
'22C = (22Z, 22Z)',
'22Z = (22B, 22B)',
'XXX = (XXX, XXX)']




if __name__ == "__main__":
    d8 = read_file("day8.txt")
    instructions, coords_dict = parse_instructions(d8)
    steps = navigate(instructions, coords_dict)
    print(steps)

    in_test3, co_test3 = parse_instructions(test3)
    steps_test3 = navigate_part2(in_test3, co_test3, verbose=True)
    print(steps_test3 == 6)
    steps2 = navigate_part2(instructions, coords_dict)
    print(steps2)