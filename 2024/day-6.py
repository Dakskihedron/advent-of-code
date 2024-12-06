# Part one
def find_distinct_guard_visits(data, start_pos):
    dir = '^'
    y, x = start_pos
    path = set([start_pos])

    while True:
        # Going up
        if dir == '^':
            path.add((y, x))
            if y > 0:
                if data[y-1][x] == '#':
                    dir = '>'
                else:
                    y -= 1
            else:
                break

        # Going right
        elif dir == '>':
            path.add((y, x))
            if x < len(data[0])-1:
                if data[y][x+1] == '#':
                    dir = 'v'
                else:
                    x += 1
            else:
                break

        # Going down
        elif dir == 'v':
            path.add((y, x))
            if y < len(data)-1:
                if data[y+1][x] == '#':
                    dir = '<'
                else:
                    y += 1
            else:
                break

        # Going left
        elif dir == '<':
            path.add((y, x))
            if x > 0:
                if data[y][x-1] == '#':
                    dir = '^'
                else:
                    x -= 1
            else:
                break

    print('Part one:', len(path))
    return path


# Part two
def find_loops(data, path, start_pos):

    def get_move(data, y, x, dir):
        # Going up
        if dir == '^':
            if y > 0:
                if data[y-1][x] == '#':
                    dir = '>'
                else:
                    y -= 1

        # Going right
        elif dir == '>':
            if x < len(data[0])-1:
                if data[y][x+1] == '#':
                    dir = 'v'
                else:
                    x += 1

        # Going down
        elif dir == 'v':
            if y < len(data)-1:
                if data[y+1][x] == '#':
                    dir = '<'
                else:
                    y += 1

        # Going left
        elif dir == '<':
            if x > 0:
                if data[y][x-1] == '#':
                    dir = '^'
                else:
                    x -= 1

        return y, x, dir

    y, x = start_pos
    sum = 0

    for pos in path:
        i, j = pos

        if data[i][j] == '#' or data[i][j] == '^':
            continue

        hy, hx, hd = y, x, '^'
        ty, tx, td = y, x, '^'

        data[i][j] = '#'

        hy, hx, hd = get_move(data, hy, hx, hd)

        while True:
            hy2, hx2, hd2 = get_move(data, hy, hx, hd)
            if (hy2, hx2, hd2) == (hy, hx, hd):
                break

            hy3, hx3, hd3 = get_move(data, hy2, hx2, hd2)
            if (hy3, hx3, hd3) == (hy2, hx2, hd2):
                break

            hy, hx, hd = hy3, hx3, hd3
            ty, tx, td = get_move(data, ty, tx, td)
            if (hy, hx, hd) == (ty, tx, td):
                sum += 1
                break

        data[i][j] = '.'

    print('Part two:', sum)


def main():
    with open('inputs/day-6.in', 'r') as file:
        data = [[_ for _ in _] for _ in file.read().strip().split('\n')]

    start_pos = (0, 0)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '^':
                start_pos = (y, x)

    path = find_distinct_guard_visits([[_ for _ in _] for _ in data], start_pos)
    find_loops([[_ for _ in _] for _ in data], path, start_pos)

if __name__ == '__main__':
    main()
