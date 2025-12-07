# Part one
def total_tachyon_beam_splits(data):
    total = 0
    cache = set()

    def recursive(x, y, data):
        nonlocal total
        nonlocal cache

        if (x,y) in cache:
            return 0

        cache.add((x,y))

        if y == len(data):
            return 1
        elif data[y][x] == '^':
            total += 1
            return recursive(x-1, y, data) + recursive(x+1, y, data)
        else:
            return recursive(x, y+1, data)


    sx, sy = 0, 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                sx = x
                sy = y

    recursive(sx, sy, data)

    print('Part one:', total)


# Part two
def total_tachyon_timelines(data):
    cache = {}

    def recursive(x, y, data):
        nonlocal cache

        if (x,y) in cache:
            return cache[(x,y)]

        if y == len(data):
            cache[(x,y)] = 1
            return 1
        elif data[y][x] == '^':
            timelines = recursive(x-1, y, data) + recursive(x+1, y, data)
            cache[(x, y)] = timelines
            return timelines
        else:
            timelines = recursive(x, y+1, data)
            cache[(x, y)] = timelines
            return timelines


    sx, sy = 0, 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                sx = x
                sy = y

    total = recursive(sx, sy, data)

    print('Part two:', total)


def main():
    with open('inputs/day-7.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [[_ for _ in _] for _ in data]

    total_tachyon_beam_splits(data)
    total_tachyon_timelines(data)


if __name__ == '__main__':
    main()
