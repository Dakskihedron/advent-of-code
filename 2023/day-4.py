from collections import deque, defaultdict
import re


# Part one and two
def scratchcards(data):
    wins = defaultdict(lambda _ : 0)
    points_total = 0
    cards_total = 0

    for line in range(len(data)):
        points = 0
        same = 0
        for i in data[line][1]:
            if i in data[line][0]:
                same += 1
        if same > 1:
            points += 1
            for _ in range(same-1):
                points = points * 2
        elif same == 1:
            points = 1
        points_total += points
        wins[line+1] = same

    q = deque()
    q.extend(list(range(1, len(data)+1)))
    while len(q) != 0:
        s = q.popleft()
        cards_total += 1
        if wins[s] > 0:
            q.extend(list(range(s+1, s+wins[s]+1)))

    print('Part one:', points_total)
    print('Part two:', cards_total)


def main():
    with open('inputs/day-4.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [line.split(':')[1] for line in data]
        data = [line.strip().split('|') for line in data]
        data = [[re.sub(' +', ' ', i) for i in line] for line in data]
        data = [[[int(n) for n in i.strip().split(' ')] for i in j] for j in data]
    scratchcards(data)


if __name__ == '__main__':
    main()