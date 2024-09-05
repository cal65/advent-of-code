from day2 import *
import re
from typing import List

class NumberSeq():
    def __init__(self, value, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.value = value
    
    def adjacent(self, plocs = List[tuple]):
        for p in plocs:
            if p[0] in range(self.x1-1, self.x2+2):
                if p[1] in range(self.y1-1, self.y2+2):
                    return True
        return False


def makeNumberSeqs(numbers, number_locations):
    rns = []
    for n, nl in zip(numbers, number_locations):
        rn = NumberSeq(value=n, 
          x1=nl[0], y1=nl[1],
          x2=nl[0], y2=nl[1] + len(str(n))-1
         )
        rns.append(rn)
    return rns
        

def findNumbers(d3):
    number_locations = []
    numbers = []
    for i in range(len(d3)):
        matches = re.finditer(r"\d+", d3[i])
        try:
            numbers_row, numerical_locations = zip(*[(int(match.group()), (i, match.start())) for match in matches])
            number_locations += numerical_locations
            numbers += numbers_row
        except:
            pass
    return numbers, number_locations


def find_symbols(d3):
    locations = []
    for i in range(len(d3)):
        matches = re.finditer(r"[^\w\s.]", d3[i])
        punctuation_locations = [ (i, match.start()) for match in matches]
        locations += punctuation_locations
    return locations


def find_asterisks(d3):
    locations = []
    for i in range(len(d3)):
        matches = re.finditer(r"\*", d3[i])
        punctuation_locations = [ (i, match.start()) for match in matches]
        locations += punctuation_locations
    return locations


def main():
    d3 = read_file('day3.txt')

    locs1 = find_symbols(d3)
    numbers, number_locations = findNumbers(d3)

    numberSeqs = makeNumberSeqs(numbers, number_locations)
    total = sum([rn.value for rn in numberSeqs if rn.adjacent(locs1)])
    print(total)
    asterisks_locations = find_asterisks(d3)
    gears = []
    for asterisk in asterisks_locations:
        adj_parts = [rn.value for rn in numberSeqs if rn.adjacent([asterisk])]
        if len(adj_parts)==2:
            gears.append(adj_parts[0] * adj_parts[1])
    print(sum(gears))
    

if __name__ == '__main__':
    main()
