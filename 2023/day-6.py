from functools import reduce
import re


# Part one
def calc_ways(data):
    data = [[int(_) for _ in re.sub(' +', ' ', _).split(':')[1].strip().split(' ')] for _ in data]
    data = {data[0][i]: data[1][i] for i in range(len(data[0]))}
    counts = []
    for time, dist in data.items():
        count = 0
        for i in range(time):
            d = i * (time - i)
            if d > dist:
                count += 1
        counts.append(count)
    print('Part one:', reduce(lambda a,b: a*b, counts))


# Part two
def calc_ways_big(data):
    time, dist = [[int(_) for _ in re.sub(' +', '', _).split(':')[1].strip().split(' ')][0] for _ in data]
    counts = 0
    for i in range(time):
        d = i * (time - i)
        if d > dist:
            counts += 1
    print('Part two:', counts)


def main():
    with open('inputs/day-6.in', 'r') as file:
        data = file.read().strip().split('\n')
    calc_ways(data)
    calc_ways_big(data)


if __name__ == '__main__':
    main()