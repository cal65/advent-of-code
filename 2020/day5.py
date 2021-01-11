import pandas as pd
import numpy as np


def read_day5(file):
    d5 = pd.read_table(file, header=None)[0]
    return d5


def evaluate_row_column(binary, front_letter, back_letter):
    id_list = list(binary)

    n = len(id_list)
    low = 0
    high = 2 ** n - 1
    for i, letter in enumerate(id_list):
        if letter == front_letter:
            low = low
            high = high - 2 ** (n - i - 1)
        if letter == back_letter:
            low = low + 2 ** (n - i - 1)
            high = high
    return low


def evaluate_seat(ticket_id):
    front_back = ticket_id[:7]
    left_right = ticket_id[7:]
    seat_id = evaluate_row_column(front_back, "F", "B") * 8 + evaluate_row_column(
        left_right, "L", "R"
    )
    return seat_id


def test_evaluate_seat():
    assert evaluate_seat("BFFFBBFRRR") == 567
    assert evaluate_seat("FFFBBBFRRR") == 119
    assert evaluate_seat("BBFFBBFRLL") == 820


if __name__ == "__main__":
    input = read_day5("day5.txt")
    seat_ids = [evaluate_seat(line) for line in input]

    seat_range = np.arange(min(seat_ids), max(seat_ids))
    missing_seats = set(seat_range).difference(set(seat_ids))
    print(max(seat_ids))
    print(missing_seats.pop())
