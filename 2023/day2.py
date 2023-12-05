import pandas as pd
import numpy as np

def read_file(file_path):
    num = pd.read_table(file_path, header=None)
    return num[0]

def parse_to_df(arr):
    splits = arr.str.split(':')
    games = [s[0] for s in splits]
    rolls = [s[1] for s in splits]
    roll_dict = {}
    for g, roll in zip(games, rolls):
        r_split = roll.split(';')
        r_series = pd.Series(r_split)
        roll_dict[g] = pd.DataFrame(r_series).T
    
    df = pd.concat(roll_dict, axis=0).reset_index()
    df.drop(columns='level_1', inplace=True)
    df.rename(columns={'level_0': 'game'}, inplace=True)
    df['game'] = df['game'].str.replace('Game ', '').astype(int)
    return df


def parse_rolls(rolls, roll_num):
    rolls_color = rolls.str.strip().str.split(', ')
    split_rolls = []
    for roll in rolls_color:
        # should be 3 in roll
        s = []
        if not isinstance(roll, list):
            break
        for r in roll:
            s.append(split_number_and_color(r))
        split_rolls.append(s)

    roll_dfs = [split_rows_to_df(s) for s in split_rolls]
    roll_dfs = pd.concat(roll_dfs).reset_index(drop=True)
    roll_dfs.columns = [f'{c}_{roll_num}' for c in roll_dfs.columns]
    roll_dfs = roll_dfs.fillna(0)
    return roll_dfs


def split_number_and_color(roll):
    raw = roll.split(' ')
    number = int(raw[0])
    color = raw[1]
    return number, color


def split_rows_to_df(split):
    series = pd.Series()
    # group by color with order being 1. green 2. blue 3. red
    color_dict = {'green': 1, 'blue': 2, 'red': 3}
    for s in split:
        color = s[1]
        n = color_dict[color]
        series[f'count_{color}'] = s[0]
        series[f'color_{n}'] = color
    df = pd.DataFrame(series).T
    return df


def eval_impossible_rolls(df, n):
    color_limits = {'green': 13, 'blue': 14, 'red': 12}
    impossible_dict = {}
    for color in ['green', 'blue', 'red']:
        roll_count_col = f'count_{color}_{n}'
        impossible_dict[color] = df[roll_count_col] > color_limits[color]
    impossible_df = pd.concat(impossible_dict, axis=1)
    # check if any of the rows are impossible
    impossible = impossible_df.apply(lambda x: any(x == True), axis=1)
    # impossible is now the T/F where T means impossible
    return impossible

    
if __name__ == "__main__":
    arr = read_file('2023/day2.txt')
    df = parse_to_df(arr)
    print(df)

    roll_dfs = {}
    for i in range(1, 5):
        roll_dfs[i] = parse_rolls(df[i], i)
    roll_dfs_all = pd.concat(roll_dfs, ignore_index=True)
    df_all = pd.concat([df, roll_dfs_all], axis=1)
    df_all['impossible_1'] = eval_impossible_rolls(df_all, n=1)
    df_all['impossible_2'] = eval_impossible_rolls(df_all, n=2)
    df_all['impossible_3'] = eval_impossible_rolls(df_all, n=3)
    df_all['impossible'] = df_all['impossible_1'] | df_all['impossible_2'] | df_all['impossible_3']
    impossible_games = df_all.loc[df_all['impossible'] == True, 'game'] 