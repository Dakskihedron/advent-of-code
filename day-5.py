with open('inputs/day-5.txt', 'r') as file:
    data = file.read().split('\n')

def to_points(coords):
    start, end = coords.strip().split(' -> ')
    start = tuple(map(int, start.split(',')))
    end = tuple(map(int, end.split(',')))
    return start, end

def get_points(start, end):
    if start < end:
        points = list(range(start, end))
    else:
        points = list(range(start, end, -1))
    points.append(end)
    return points

# Part one
plot = [[0] * 1000 for i in range(1000)]

for line in data:
    coords = to_points(line)
    # If diagonal
    if coords[0][0] != coords[1][0] and coords[0][1] != coords[1][1]:
        continue
    # If x1 = x2
    if coords[0][0] == coords[1][0]:
        points = get_points(coords[0][1], coords[1][1])
        for p in points:
            plot[p][coords[0][0]] += 1
    else:
        # If y1 = y2
        points = get_points(coords[0][0], coords[1][0])
        for p in points:
            plot[coords[0][1]][p] += 1

overlaps = 0
for s in range(len(plot)):
    for p in range(len(plot[s])):
        if plot[s][p] > 1:
            overlaps += 1
print(overlaps)

# Part two
plot = [[0] * 1000 for i in range(1000)]

for line in data:
    coords = to_points(line)
    # If diagonal
    if coords[0][0] != coords[1][0] and coords[0][1] != coords[1][1]:
        points_x = get_points(coords[0][0], coords[1][0])
        points_y = get_points(coords[0][1], coords[1][1])
        for p in range(len(points_x)):
            plot[points_y[p]][points_x[p]] += 1
    # If x1 = x2
    elif coords[0][0] == coords[1][0]:
        points = get_points(coords[0][1], coords[1][1])
        for p in points:
            plot[p][coords[0][0]] += 1
    else:
        # If y1 = y2
        points = get_points(coords[0][0], coords[1][0])
        for p in points:
            plot[coords[0][1]][p] += 1

overlaps = 0
for s in range(len(plot)):
    for p in range(len(plot[s])):
        if plot[s][p] > 1:
            overlaps += 1
print(overlaps)