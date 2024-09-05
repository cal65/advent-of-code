import pandas as pd

def read_day6(file):
    d6 = pd.read_table(file, header=None, skip_blank_lines=F)[0]
    return d6