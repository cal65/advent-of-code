

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


def calc_copies(scores):
    card_matches = [int(np.log2(s))+1 if s >0 else 0 for s in scores]
    multiplier_dict = {}
    for i in range(len(card_matches)):
        multiplier_dict[i] = 1
    card_copies = []
    for i, cm in enumerate(card_matches):
        copies = multiplier_dict[i]
        card_copies.append(copies)
        if cm > 0:
            for j in range(int(cm)):
                multiplier_dict[i+j+1] += 1*copies
    return multiplier_dict


    