from functools import reduce
from collections import defaultdict, OrderedDict
import re


# Part one
def hash(seq):
    return (seq * 17) % 256


def init(data):
    print('Part one:', sum([reduce(lambda a,b: hash(a + ord(b)), x, 0) for x in data]))


# Part two
def focusing_power(data):
    hashmap = defaultdict(OrderedDict)
    data = [re.split(r"(\W)", x) for x in data]

    for group in data:
        box = reduce(lambda a,b: hash(a + ord(b)), [_ for _ in group[0]], 0)
        if group[1] == '-':
            if group[0] in hashmap[box]:
                hashmap[box].pop(group[0])
        else:
            hashmap[box][group[0]] = group[2]

    power = 0
    for box in hashmap.keys():
        for k,v in hashmap[box].items():
            power += ((1+box) * (list(hashmap[box].keys()).index(k)+1) * int(v))

    print('Part two:', power)


def main():
    with open('inputs/day-15.in', 'r') as file:
        data = file.read().strip().split(',')
    init(data)
    focusing_power(data)


if __name__ == '__main__':
    main()