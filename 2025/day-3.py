import copy
import itertools


# Part one
def calculate_max_joltage_for_two_battery_banks(data):
    sum = 0

    for i in range(len(data)):
        combinations = list(itertools.combinations(data[i], 2))
        sum += max([int(str(_[0]) + str(_[1])) for _ in combinations])

    print('Part one:', sum)


# Part two
def calculate_max_joltage_for_12_battery_banks(data):
    sum = 0

    for i in range(len(data)):
        line = data[i]
        n = copy.deepcopy(line)

        while len(n) != 12:
            l = 0
            largest = None
            for i in range(len(n)):
                x = copy.deepcopy(n)
                x.pop(i)
                y = int(''.join([str(_) for _ in x]))
                if y > l:
                    l = y
                    largest = x

            n = largest

        sum += int(''.join([str(_) for _ in n]))

    print('Part two:', sum)


def main():
    with open('inputs/day-3.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [[int(_) for _ in _] for _ in data]

    calculate_max_joltage_for_two_battery_banks(data)
    calculate_max_joltage_for_12_battery_banks(data)


if __name__ == '__main__':
    main()
