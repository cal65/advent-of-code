from day2 import read_file
import numpy as np
import pandas as pd


def split_text(d7):
    # split the text into a list of lists
    # each list is a rule
    hands, bids = zip(*[d.split(" ") for d in d7])
    return hands, bids

mapper = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


def parse_hand(hand):
    vals_dict = {}
    for card in hand:
        if card in vals_dict.keys():
            vals_dict[card] += 1
        else:
            vals_dict[card] = 1
    return vals_dict

def parse_hand_part2(hand, mapper2):
    vals_dict = {}
    for card in hand:
        if card in vals_dict.keys():
            vals_dict[card] += 1
        else:
            vals_dict[card] = 1
    if 'J' in vals_dict.keys():
        if len(vals_dict.keys()) ==1:
            ## edge case of 5 J's
            return vals_dict
        vals_dict = sort_dict_custom(vals_dict, hierarchy=list(mapper2.keys()))
        j_number = vals_dict['J']
        del vals_dict['J']
        c = getMax(vals_dict)
        vals_dict[c] += j_number
        
    return vals_dict

def sort_dict_custom(d, hierarchy=list(mapper.keys())):
    # Sort by values in reverse order and by custom hierarchy in normal order when values are the same
    sorted_dict = dict(
        sorted(
            d.items(),
            key=lambda item: (-item[1], hierarchy.index(item[0]))
        )
    )
    return sorted_dict

def getMax(vals_dict):
    max_card = max(vals_dict, key=vals_dict.get)
    return max_card



def tie_break(hand, mapper):
    tie_breaker = 0
    tie_breaker += mapper[hand[0]] # tie breaker is the value of the first card
    tie_breaker += mapper[hand[1]]/(13**1)
    tie_breaker += mapper[hand[2]]/(13**2)
    tie_breaker += mapper[hand[3]]/(13**3)
    tie_breaker += mapper[hand[4]]/(13**4)
    return tie_breaker


def hand_to_int(hand, mapper=mapper, part2=False, mapper2=None):
    if part2:
        if mapper is None:
            mapper2 = mapper
        vals_dict = parse_hand_part2(hand, mapper2)
    else:
        vals_dict = parse_hand(hand)
    vals = [v for v in vals_dict.values()]
    # convert the hand to a numeric value that can be sorted
    # 5 of a kind can be 78 + card value
    # high card is 0 + card value
    max_mapper = {
        1: 0,
        2: 13,
        3: 13 * 3,
        4: 13 * 5,
        5: 13 * 6,
    }  # extra spacing for 2 pair and full house
    total = max_mapper[max(vals)]
    # get the second highest value
    vals.remove(max(vals))
    if len(vals) > 0:
        # if there is a second highest value and not 5 of a kind
        second_highest = max(vals)
    else:
        second_highest = 0
    if second_highest > 1:
        # this is for 2 pair and full house
        total += 13
        # del vals_dict[max_card]
        # second_highest_card = max(vals_dict, key=vals_dict.get)
        # total += mapper[second_highest_card]/13 # tibreaking between pairs of the same
        
    total += tie_break(hand, mapper)
    # so we want high card to be between 0 and 13
    # pair to be between 13 and 26
    # 2 pair to be between 26 and 39
    # 3 of a kind to be between 39 and 52
    # full house to be between 52 and 65
    # 4 of a kind to be between 65 and 78
    # 5 of a kind to be between 78 and 91
    return total

def grade_hand(vals_dict):
    vals = [v for v in vals_dict.values()]
    # convert the hand to a numeric value that can be sorted
    # 5 of a kind can be 78 + card value
    # high card is 0 + card value
    max_mapper = {
        1: 'high card',
        2: 'pair',
        3: 'three of a kind',
        4: 'four of a kind',
        5: 'five of a kind',
    }  # extra spacing for 2 pair and full house
    hand_str = max_mapper[max(vals)]
    vals.remove(max(vals))
    if len(vals) > 0:
        # if there is a second highest value and not 5 of a kind
        second_highest = max(vals)
        if second_highest > 1:
            if hand_str == 'pair':
                hand_str = 'two pair'
            elif hand_str == 'three of a kind':
                hand_str = 'full house'
    return hand_str
    



def calc_winnings_df(hands, scores, bids):
    df = pd.DataFrame({"hand": hands, "score": scores, "bid": bids})
    df['rank'] = df['score'].rank(ascending=True)
    df['winnings'] = df['bid'].astype(int) * df['rank']
    #df.sort_values('rank', inplace=True)
    return df


def winnings_pipeline(hands, bids, part2=False, mapper2=None):
    scores = [hand_to_int(h, part2=part2, mapper2=mapper2) for h in hands]
    winnings_df = calc_winnings_df(hands, scores, bids)
    return winnings_df


if __name__ == "__main__":
    d7 = read_file("day7.txt")
    test_hands = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    test_hands, test_bids = split_text(test_hands)
    test_scores = [hand_to_int(h) for h in test_hands]
    test_df = pd.DataFrame({"hand": test_hands, "score": test_scores, "bid": test_bids})
    test_df['rank'] = test_df['score'].rank(ascending=True)
    print(test_df)
    test_df['winnings'] = test_df['bid'].astype(int) * test_df['rank']
    print(test_df['winnings'].sum() == 6440)
    hands, bids = split_text(d7)
    scores = [hand_to_int(h) for h in hands]
    winnings_df = calc_winnings_df(hands, scores, bids)
    print(winnings_df.head())
    print(winnings_df.loc[winnings_df['hand'].isin(['45455', 'J444J'])])
    print(winnings_df['winnings'].sum())
    ## part 2
    mapper_part2 = mapper.copy()
    for v in ['T', '9', '8', '7', '6', '5', '4', '3', '2']:
        mapper_part2[v] = mapper[v] + 1
    del mapper_part2['J']
    mapper_part2['J'] = 0
    
    print("Test Part 2")
    test_part2 = winnings_pipeline(test_hands, test_bids, part2=True, mapper2=mapper_part2)['winnings'].sum()==5905
    print(test_part2)
    
    scores_part2 = [hand_to_int(h, mapper=mapper_part2, part2=True, mapper2=mapper_part2) for h in hands]
    print(calc_winnings_df(hands, scores_part2, bids)['winnings'].sum())
    # 251824095.0