with open('inputs/day-9.txt') as file:
    data = file.read().split('\n')
    data = [list(map(int, x)) for x in data]

# Part one
def is_smaller(val, val_list):
    for x in val_list:
        if val >= data[x[0]][x[1]]:
            return False
    return True

def get_adjacent(y, x):
    adjacent = []
    if y > 0:
        adjacent.append((y-1, x))
    if y < len(data) - 1:
        adjacent.append((y+1, x))
    if x > 0:
        adjacent.append((y, x-1))
    if x < len(data[y]) - 1:
        adjacent.append((y, x+1))
    return adjacent

risk = 0
lowpoints = []
for y in range(len(data)):
    for x in range(len(data[y])):
        adjacent = get_adjacent(y, x)
        if is_smaller(data[y][x], adjacent):
            lowpoints.append((y, x))
            risk += data[y][x] + 1
print(risk)

# Part two
def floodfill(y, x, data):
    if data[y][x] == 9:
        return 0
    data[y][x] = 9
    area = 1
    if y > 0:
        area += floodfill(y-1, x, data)
    if y < len(data) - 1:
        area += floodfill(y+1, x, data)
    if x > 0:
        area += floodfill(y, x-1, data)
    if x < len(data[y]) - 1:
        area += floodfill(y, x+1, data)
    return area

basins = []
for l in lowpoints:
    basin_data = list(list(i) for i in data)
    basins.append(floodfill(l[0], l[1], basin_data))
basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])