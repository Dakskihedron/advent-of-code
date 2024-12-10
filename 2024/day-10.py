# Part one
def total_trailhead_scores(data, trailheads):

    def find_trail(prev, y, x, data, seen):
        if (y, x) in seen:
            return 0

        if x < 0 or x > len(data[0])-1 or y < 0 or y > len(data)-1:
            return 0

        if data[y][x] != (prev + 1):
            return 0

        if data[y][x] == 9:
            seen.append((y, x))
            return 1

        prev = data[y][x]
        seen.append((y, x))

        return find_trail(prev, y, x-1, data, seen) \
            + find_trail(prev, y, x+1, data, seen) \
            + find_trail(prev, y-1, x, data, seen) \
            + find_trail(prev, y+1, x, data, seen)

    sum = 0
    for trailhead in trailheads:
        y, x = trailhead
        sum += find_trail(-1, y, x, data, [])

    print('Part one:', sum)


# Part two
def total_trailhead_ratings(data, trailheads):

    def find_trail(prev, y, x, data):
        if x < 0 or x > len(data[0])-1 or y < 0 or y > len(data)-1:
            return 0

        if data[y][x] != (prev + 1):
            return 0

        if data[y][x] == 9:
            return 1

        prev = data[y][x]
        return find_trail(prev, y, x-1, data) \
            + find_trail(prev, y, x+1, data) \
            + find_trail(prev, y-1, x, data) \
            + find_trail(prev, y+1, x, data)

    sum = 0
    for trailhead in trailheads:
        y, x = trailhead
        sum += find_trail(-1, y, x, data)

    print('Part two:', sum)


def main():
    with open('inputs/day-10.in', 'r') as file:
        data = [[int(_) for _ in _] for _ in file.read().strip().split('\n')]

    trailheads = []
    for y in range(len(data)):
        for x in range(len(data)):
            if data[y][x] == 0:
                trailheads.append((y, x))

    total_trailhead_scores(data, trailheads)
    total_trailhead_ratings(data, trailheads)

if __name__ == '__main__':
    main()
