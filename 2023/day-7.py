from functools import cmp_to_key
from collections import Counter


# Part one
def get_type(cards):
    counts = Counter(cards).values()
    if len(counts) == 5:
        return 0
    if len(counts) == 4:
        return 1
    if len(counts) == 3:
        if 3 in counts:
            return 3
        return 2
    if len(counts) == 2:
        if 4 in counts:
            return 5
        return 4
    else:
        return 6
        

def cc_cmp(a, b):
    ord = '23456789TJQKA'
    if get_type(a) > get_type(b):
        return 1
    elif get_type(a) < get_type(b):
        return -1
    else:
        for i in range(5):
            if ord.index(a[i]) > ord.index(b[i]):
                return 1
            elif ord.index(a[i]) < ord.index(b[i]):
                return -1
    return 0


def camel_cards(data, lookup):
    sorted_data = sorted(data, key=cmp_to_key(cc_cmp))
    winnings = 0
    for i in range(len(data)):
        winnings += (i+1) * lookup[sorted_data[i]]
    print('Part one:', winnings)


# Part two
def get_type_joker(cards):
    keys = Counter(cards).keys()
    counts = Counter(cards).values()
    if len(counts) == 5:
        if 'J' in keys:
            return 1
        return 0
    if len(counts) == 4:
        if 'J' in keys:
            return 3
        return 1
    if len(counts) == 3:
        if 3 in counts:
            if 'J' in keys:
                return 5
            return 3
        if 'J' in keys:
            return Counter(cards)['J'] + 3
        return 2
    if len(counts) == 2:
        if 4 in counts:
            if 'J' in keys:
                return 6
            return 5
        if 'J' in keys:
            return 6
        return 4
    else:
        return 6


def cc_cmp_joker(a, b):
    ord = 'J23456789TQKA'
    if get_type_joker(a) > get_type_joker(b):
        return 1
    elif get_type_joker(a) < get_type_joker(b):
        return -1
    else:
        for i in range(5):
            if ord.index(a[i]) > ord.index(b[i]):
                return 1
            elif ord.index(a[i]) < ord.index(b[i]):
                return -1
    return 0


def camel_cards_joker(data, lookup):
    sorted_data = sorted(data, key=cmp_to_key(cc_cmp_joker))
    winnings = 0
    for i in range(len(data)):
        winnings += (i+1) * lookup[sorted_data[i]]
    print('Part two:', winnings)


def main():
    with open('inputs/day-7.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [_.split(' ') for _ in data]
        data = {_[0]: int(_[1]) for _ in data}
    camel_cards(list(data.keys()), data)
    camel_cards_joker(list(data.keys()), data)


if __name__ == '__main__':
    main()