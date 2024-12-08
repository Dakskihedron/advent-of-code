# Part one
def find_unique_antinodes(points, max_x, max_y):
    antinodes = set()

    for m in points:
        for n in points:
            if m != n and m[2] == n[2]:
                x = ((n[0] - m[0]) * 2) + m[0]
                y = ((n[1] - m[1]) * 2) + m[1]

                if 0 <= x <= max_x and 0 <= y <= max_y:
                    antinodes.add((x, y))

    print('Part one:', len(antinodes))


# Part two
def find_all_unique_antinodes(points, max_x, max_y):
    antinodes = set()

    for m in points:
        for n in points:
            if m != n and m[2] == n[2]:
                dx, dy = n[0] - m[0], n[1] - m[1]
                x, y = m[0], m[1]

                while True:
                    x += dx
                    y += dy

                    if 0 <= x <= max_x and 0 <= y <= max_y:
                        antinodes.add((x, y))
                    else:
                        break

    print('Part two:', len(antinodes))


def main():
    with open('inputs/day-8.in', 'r') as file:
        data = [[_ for _ in _] for _ in file.read().strip().split('\n')]
        max_x = len(data[0]) - 1
        max_y = len(data) - 1
        points = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != '.':
                    points.append((j, i, data[i][j]))

    find_unique_antinodes(points, max_x, max_y)
    find_all_unique_antinodes(points, max_x, max_y)

if __name__ == '__main__':
    main()
