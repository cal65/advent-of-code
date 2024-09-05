

def strip_split(text):
    stripped_array = text.strip().split(' ')
    stripped_aray = [s for s in stripped_array if s != '']
    return stripped_aray


def split_cards(d4):
    numbers = [d.split(":")[1] for d in d4]
    n1s, n2s = zip(*[n.split('|') for n in numbers])
    n1_array = [strip_split(n) for n in n1s]
    n2_array = [strip_split(n) for n in n2s]
    return n1_array, n2_array


def calc_card_scores(n1_array, n2_array):
    scores = []
    for n1, n2 in zip(n1_array, n2_array):
        winning = set(n1).intersection(set(n2))
        lw = len(winning)
        if lw > 0:
            scores.append(2**(lw-1))
        else:
            scores.append(0)
    return scores


    