with open('inputs/day-15.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [x.replace(':', '').replace(',', '').split(' ') for x in data]
    data = [[(int(x[2][2:]), int(x[3][2:])), (int(x[8][2:]), int(x[9][2:]))] for x in data]


# Part one
def calc_positions(level, data):
    occupied = [x for y in data for x in y if x[1] == level]
    positions = set()

    for i in data:
        sensor = i[0]
        beacon = i[1]
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        if level <= sensor[1] + dist and level >= sensor[1] - dist:
            offset = abs(level - sensor[1])
            minx = sensor[0] - dist + offset
            maxx = sensor[0] + dist - offset

            for x in [*range(minx, maxx + 1)]:
                pos = (x, level)
                if pos not in occupied:
                    positions.add(pos)

    return positions

print('Part 1:', len(calc_positions(2000000, data)))


# Part two (terribly unoptimised; give it a minute or two)
def calc_tuning_freq(data):
    outer = {}

    for i in data:
        sensor = i[0]
        beacon = i[1]
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        if (sensor[0], sensor[1] - dist - 1) in outer:
            outer[(sensor[0], sensor[1] - dist - 1)] += 1
        else:
            outer[(sensor[0], sensor[1] - dist - 1)] = 0

        if (sensor[0], sensor[1] + dist + 1) in outer:
            outer[(sensor[0], sensor[1] + dist + 1)] += 1
        else:
            outer[(sensor[0], sensor[1] + dist + 1)] = 0

        for y in range(sensor[1] - dist, sensor[1] + dist + 1):
            offset = abs(y - sensor[1])

            if (sensor[0] - dist - 1 + offset, y) in outer:
                outer[(sensor[0] - dist - 1 + offset, y)] += 1
            else:
                outer[(sensor[0] - dist - 1 + offset, y)] = 0

            if (sensor[0] + dist + 1 - offset, y) in outer:
                outer[(sensor[0] + dist + 1 - offset, y)] += 1
            else:
                outer[(sensor[0] + dist + 1 - offset, y)] = 0

    highest = max(outer.values())
    coords = [k for k in outer.keys() if outer[k] == highest]

    return coords

for c in calc_tuning_freq(data):
    if not c in calc_positions(c[1], data) and c[0] >= 0 and c[1] <= 4000000:
        print('Part 2:', c[0] * 4000000 + c[1])