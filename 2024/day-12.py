# Part one
def total_fencing_price(data):
    regions = {}
    global_seen = set()
    max_x = len(data[0]) - 1
    max_y = len(data) - 1

    def floodfill(type, seen, y, x):
        if (y,x) in seen:
            return 0

        if data[y][x] != type:
            return 1
        
        seen.add((y,x))
        global_seen.add((y,x))

        p = 0

        if y > 0:
            p += floodfill(type, seen, y-1, x)
        else:
            p += 1

        if y < max_y:
            p += floodfill(type, seen, y+1, x)
        else:
            p += 1

        if x > 0:
            p += floodfill(type, seen, y, x-1)
        else:
            p += 1

        if x < max_x:
            p += floodfill(type, seen, y, x+1)
        else:
            p += 1

        return p

    sum = 0
    i = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (y,x) not in global_seen:
                seen = set()
                sum += floodfill(data[y][x], seen, y, x) * len(seen)
                regions[(i, data[y][x])] = seen
                i += 1

    print('Part one:', sum)
    return regions


# Part two
def total_fencing_price_by_sides(data, regions):
    max_x = len(data[0]) - 1
    max_y = len(data) - 1

    sum = 0
    for region in regions:
        coords = regions[region]
        _, type = region
        corners = 0

        for c in coords:
            y, x = c

            # NE
            if (y-1 >= 0 and x+1 <= max_x):
                if data[y-1][x] == type and data[y][x+1] == type:
                    if data[y-1][x+1] != type:
                        corners += 1
                elif data[y-1][x] != type and data[y][x+1] != type:
                    corners += 1
            elif (y-1 < 0 and x+1 > max_x):
                corners += 1
            elif y-1 < 0 and x+1 <= max_x:
                if data[y][x+1] != type:
                    corners += 1
            elif x+1 > max_x and y-1 >= 0:
                if data[y-1][x] != type:
                    corners += 1

            # SE
            if (x+1 <= max_x and y+1 <= max_y):
                if data[y+1][x] == type and data[y][x+1] == type:
                    if data[y+1][x+1] != type:
                        corners += 1
                elif data[y+1][x] != type and data[y][x+1] != type:
                    corners += 1
            elif (x+1 > max_x and y+1 > max_y):
                corners += 1
            elif x+1 > max_x and y+1 <= max_y:
                if data[y+1][x] != type:
                    corners += 1
            elif y+1 > max_y and x+1 <= max_x:
                if data[y][x+1] != type:
                    corners += 1

            # SW
            if (y+1 <= max_y and x-1 >= 0):
                if data[y+1][x] == type and data[y][x-1] == type:
                    if data[y+1][x-1] != type:
                        corners += 1
                elif data[y+1][x] != type and data[y][x-1] != type:
                    corners += 1
            elif (y+1 > max_y and x-1 < 0):
                corners += 1
            elif y+1 > max_y and x-1 >= 0:
                if data[y][x-1] != type:
                    corners += 1
            elif x-1 < 0 and y+1 <= max_y:
                if data[y+1][x] != type:
                    corners += 1

            # NW
            if (x-1 >= 0 and y-1 >= 0):
                if data[y][x-1] == type and data[y-1][x] == type:
                    if data[y-1][x-1] != type:
                        corners += 1
                elif data[y][x-1] != type and data[y-1][x] != type:
                    corners += 1
            elif (x-1 < 0 and y-1 < 0):
                corners += 1
            elif x-1 < 0 and y-1 >= 0:
                if data[y-1][x] != type:
                    corners += 1
            elif y-1 < 0 and x-1 >= 0:
                if data[y][x-1] != type:
                    corners += 1

        sum += corners * len(coords)

    print('Part two:', sum)


def main():
    with open('inputs/day-12.in', 'r') as file:
        data = [[_ for _ in _] for _ in file.read().strip().split('\n')]

    regions = total_fencing_price(data)
    total_fencing_price_by_sides(data, regions)

if __name__ == '__main__':
    main()
