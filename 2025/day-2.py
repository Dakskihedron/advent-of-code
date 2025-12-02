import re


# Part one
def total_invalid_ids_occurring_twice(data):
    sum = 0
    exp = re.compile(r'^(.+)\1$')

    for i in range(len(data)):
        for n in range(data[i][0], data[i][1] + 1):
            s = str(n)
            match = re.search(exp, s)
            if (match != None) and (len(match.group(0)) == len(s)):
                sum += n

    print('Part one:', sum)


# Part two
def total_invalid_ids_occurring_at_least_twice(data):
    sum = 0
    exp = re.compile(r'^(.+)\1+$')

    for i in range(len(data)):
        for n in range(data[i][0], data[i][1] + 1):
            s = str(n)
            match = re.search(exp, s)
            if (match != None) and (len(match.group(0)) == len(s)):
                sum += n

    print('Part two:', sum)


def main():
    with open('inputs/day-2.in', 'r') as file:
        data = file.read().strip().split(',')
        data = [[int(_.split('-')[0]), int(_.split('-')[1])] for _ in data]

    total_invalid_ids_occurring_twice(data)
    total_invalid_ids_occurring_at_least_twice(data)


if __name__ == '__main__':
    main()
