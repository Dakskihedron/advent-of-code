from functools import reduce
import numpy as np


# Part one and two
def find_extrapolated_sums(data):
    for_sum = 0
    rev_sum = 0
    for values in data:
        starts = []
        ends = []

        while len(set(values)) != 1:
            diffs = list(np.diff(values))
            starts.append(values.pop())
            ends.append(values.pop(0))
            values = diffs

        for_sum += sum(starts) + values[0]
        ends.append(values[0])
        rev_sum += reduce(lambda a,b: b-a, list(reversed(ends)))
        
    print('Part one:', for_sum)
    print('Part two:', rev_sum)


def main():
    with open('inputs/day-9.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [list(map(int, _.split(' '))) for _ in data]
    find_extrapolated_sums(data)


if __name__ == '__main__':
    main()