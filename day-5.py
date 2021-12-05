with open('inputs/day-5.txt', 'r') as file:
    inputs = file.read().split('\n')
    for i in range(len(inputs)):
        inputs[i] = inputs[i].split('->')
        for c in range(len(inputs[i])):
            inputs[i][c] = [int(x) for x in inputs[i][c].strip().split(',')]

def get_points(start, end):
    if start < end:
        points = list(range(start, end))
    else:
        points = list(range(start, end, -1))
    points.append(end)
    return points

# Part one
plot = [[0] * 1000 for i in range(1000)]

for coord_set in inputs:
    # If diagonal
    if coord_set[0][0] != coord_set[1][0] and coord_set[0][1] != coord_set[1][1]:
        continue
    # If x1 = x2
    if coord_set[0][0] == coord_set[1][0]:
        points = get_points(coord_set[0][1], coord_set[1][1])
        for p in points:
            plot[p][coord_set[0][0]] += 1
    else:
        # If y1 = y2
        points = get_points(coord_set[0][0], coord_set[1][0])
        for p in points:
            plot[coord_set[0][1]][p] += 1

overlap_points = 0
for s in range(len(plot)):
    for p in range(len(plot[s])):
        if plot[s][p] > 1:
            overlap_points += 1
print(overlap_points)

# Part two
plot = [[0] * 1000 for i in range(1000)]

for coord_set in inputs:
    # If diagonal
    if coord_set[0][0] != coord_set[1][0] and coord_set[0][1] != coord_set[1][1]:
        points_x = get_points(coord_set[0][0], coord_set[1][0])
        points_y = get_points(coord_set[0][1], coord_set[1][1])
        for i in range(len(points_x)):
            plot[points_y[i]][points_x[i]] += 1
    # If x1 = x2
    elif coord_set[0][0] == coord_set[1][0]:
        points = get_points(coord_set[0][1], coord_set[1][1])
        for p in points:
            plot[p][coord_set[0][0]] += 1
    else:
        # If y1 = y2
        points = get_points(coord_set[0][0], coord_set[1][0])
        for p in points:
            plot[coord_set[0][1]][p] += 1

overlap_points = 0
for s in range(len(plot)):
    for p in range(len(plot[s])):
        if plot[s][p] > 1:
            overlap_points += 1
print(overlap_points)