from copy import deepcopy

# Part one
def sum_of_all_gps_coords(warehouse, moves, start_pos):

    def move(dy, dx, cy, cx, m):
        if warehouse[cy+dy][cx+dx] == '.':
            warehouse[cy][cx], warehouse[cy+dy][cx+dx] = warehouse[cy+dy][cx+dx], warehouse[cy][cx]
            return cy+dy, cx+dx

        if warehouse[cy+dy][cx+dx] == '#':
            return cy, cx

        pos = [(cy, cx)]
        if m == '^':
            for y in range(cy-1, -1, -1):
                if warehouse[y][cx] == '#':
                    return cy, cx
                if warehouse[y][cx] == 'O':
                    pos.append((y, cx))
                if warehouse[y][cx] == '.':
                    pos.append((y, cx))
                    break
        
        if m == '>':
            for x in range(cx+1, len(warehouse[0])):
                if warehouse[cy][x] == '#':
                    return cy, cx
                if warehouse[cy][x] == 'O':
                    pos.append((cy, x))
                if warehouse[cy][x] == '.':
                    pos.append((cy, x))
                    break
        
        if m == 'v':
            for y in range(cy+1, len(warehouse)):
                if warehouse[y][cx] == '#':
                    return cy, cx
                if warehouse[y][cx] == 'O':
                    pos.append((y, cx))
                if warehouse[y][cx] == '.':
                    pos.append((y, cx))
                    break
        
        if m == '<':
            for x in range(cx-1, -1, -1):
                if warehouse[cy][x] == '#':
                    return cy, cx
                if warehouse[cy][x] == 'O':
                    pos.append((cy, x))
                if warehouse[cy][x] == '.':
                    pos.append((cy, x))
                    break

        for i in range(len(pos)-1, 0, -1):
            my, mx = pos[i]
            ny, nx = pos[i-1]
            warehouse[my][mx], warehouse[ny][nx] = warehouse[ny][nx], warehouse[my][mx]
        return cy+dy, cx+dx

    y, x = start_pos

    for m in moves:
        # Move up 
        if m == '^':
            y, x = move(-1, 0, y, x, m)

        # Move right
        if m == '>':
            y, x = move(0, 1, y, x, m)

        # Move down
        if m == 'v':
            y, x = move(1, 0, y, x, m)

        # Move left
        if m == '<':
            y, x = move(0, -1, y, x, m)

    sum = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == 'O':
                sum += (100 * i + j)

    print('Part one:', sum)


# Part two
def sum_of_all_gps_coords_2x(warehouse, moves, start_pos):
    warehouse_2x = [['.' for _ in range(len(warehouse[0]) * 2)] for _ in range(len(warehouse))]

    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            tile = warehouse[y][x]

            if (tile == '@'):
                warehouse_2x[y][x*2] = '@'
            elif tile == 'O':
                warehouse_2x[y][x*2] = '['
                warehouse_2x[y][(x*2)+1] = ']'
            else:
                warehouse_2x[y][x*2] = tile
                warehouse_2x[y][(x*2)+1] = tile

    y, x = start_pos[0], start_pos[1] * 2

    def find_boxes(cy, cx, dy):
        seen = set()
        stack = []

        stack.append((cy, cx))

        while len(stack) != 0:
            tile = stack.pop(0)
            if tile not in seen:
                seen.add(tile)
                y, x = tile

                next_tile = warehouse_2x[y+dy][x]
                if next_tile == '#':
                    return None
                
                if next_tile == '[':
                    left_coord = (y+dy, x)
                    if left_coord not in seen:
                        stack.append(left_coord)
                    right_coord = (y+dy, x+1)
                    if right_coord not in seen:
                        stack.append(right_coord)

                elif next_tile == ']':
                    left_coord = (y+dy, x)
                    if left_coord not in seen:
                        stack.append(left_coord)
                    right_coord = (y+dy, x-1)
                    if right_coord not in seen:
                        stack.append(right_coord)

        return sorted(list(seen))

    def move(dy, dx, cy, cx, m):
        if warehouse_2x[cy+dy][cx+dx] == '.':
            warehouse_2x[cy][cx], warehouse_2x[cy+dy][cx+dx] = warehouse_2x[cy+dy][cx+dx], warehouse_2x[cy][cx]
            return cy+dy, cx+dx

        if warehouse_2x[cy+dy][cx+dx] == '#':
            return cy, cx

        if m == '^':
            boxes = find_boxes(cy, cx, -1)
            if not boxes:
                return cy, cx

            for b in boxes:
                y, x = b
                warehouse_2x[y][x], warehouse_2x[y-1][x] = warehouse_2x[y-1][x], warehouse_2x[y][x]

            return cy-1, cx

        if m == '>':
            pos = [(cy, cx)]
            for x in range(cx+1, len(warehouse_2x[0])):
                if warehouse_2x[cy][x] == '#':
                    return cy, cx
                if warehouse_2x[cy][x] in ('[', ']'):
                    pos.append((cy, x))
                if warehouse_2x[cy][x] == '.':
                    pos.append((cy, x))
                    break

            for i in range(len(pos)-1, 0, -1):
                my, mx = pos[i]
                ny, nx = pos[i-1]
                warehouse_2x[my][mx], warehouse_2x[ny][nx] = warehouse_2x[ny][nx], warehouse_2x[my][mx]
            return cy+dy, cx+dx

        if m == 'v':
            boxes = find_boxes(cy, cx, 1)
            if not boxes:
                return cy, cx

            for b in reversed(boxes):
                y, x = b
                warehouse_2x[y][x], warehouse_2x[y+1][x] = warehouse_2x[y+1][x], warehouse_2x[y][x]

            return cy+1, cx

        if m == '<':
            pos = [(cy, cx)]
            for x in range(cx-1, -1, -1):
                if warehouse_2x[cy][x] == '#':
                    return cy, cx
                if warehouse_2x[cy][x] in ('[', ']'):
                    pos.append((cy, x))
                if warehouse_2x[cy][x] == '.':
                    pos.append((cy, x))
                    break

            for i in range(len(pos)-1, 0, -1):
                my, mx = pos[i]
                ny, nx = pos[i-1]
                warehouse_2x[my][mx], warehouse_2x[ny][nx] = warehouse_2x[ny][nx], warehouse_2x[my][mx]
            return cy+dy, cx+dx

    for m in moves:
        # Move up 
        if m == '^':
            y, x = move(-1, 0, y, x, m)

        # Move right
        if m == '>':
            y, x = move(0, 1, y, x, m)

        # Move down
        if m == 'v':
            y, x = move(1, 0, y, x, m)

        # Move left
        if m == '<':
            y, x = move(0, -1, y, x, m)

    sum = 0
    for i in range(len(warehouse_2x)):
        for j in range(len(warehouse_2x[0])):
            if warehouse_2x[i][j] == '[':
                sum += (100 * i + j)

    print('Part two:', sum)


def main():
    with open('inputs/day-15.in', 'r') as file:
        data = file.read().strip().split('\n')
        space = data.index('')
        warehouse = [[_ for _ in _] for _ in data[:space]]
        moves = [_ for _ in data[space+1:] for _ in _]

        start_pos = None
        for y in range(len(warehouse)):
            for x in range(len(warehouse[0])):
                if warehouse[y][x] == '@':
                    start_pos = (y, x)

    sum_of_all_gps_coords(deepcopy(warehouse), moves, start_pos)
    sum_of_all_gps_coords_2x(deepcopy(warehouse), moves, start_pos)


if __name__ == '__main__':
    main()
