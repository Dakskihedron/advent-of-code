import copy

with open('inputs/day-14.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [[tuple([int(z) for z in y.strip().split(',')]) for y in x.split('->')] for x in data]


# Part one
world = {}
height = 0

for m in range(len(data)):
    if len(data[m]) == 1:
        world[data[m][0]] = '#'
        if data[m][0][1] > height:
            height = data[m][0][1]
    else:
        for i, j in zip(data[m], data[m][1:]):
            if i[1] > height:
                height = i[1]
            if j[1] > height:
                height = j[1]

            if i[0] == j[0]:
                ymin, ymax = min([i[1], j[1]]), max([i[1], j[1]])
                for y in range(ymin, ymax + 1):
                    world[(i[0], y)] = '#'
            else:
                xmin, xmax = min([i[0], j[0]]), max([i[0], j[0]])
                for x in range(xmin, xmax + 1):
                    world[(x, i[1])] = '#'


def calculate_move(pos, new_pos, world):
    if world.get(new_pos, '.') == '.':
        return new_pos
    elif world.get((pos[0] - 1, pos[1] + 1), '.') == '.':
        return (pos[0] - 1, pos[1] + 1)
    elif world.get((pos[0] + 1, pos[1] + 1), '.') == '.':
        return (pos[0] + 1, pos[1] + 1)
    return None


def simulate_sand(world, height, floor=False):
    units = 0
    pos = (500, 0)

    while True:
        if floor:
            if world.get((500, 0), '+') == 'o':
                break

        new_pos = (pos[0], pos[1] + 1)

        if not floor:
            if new_pos[1] > height:
                break
        else:
            if new_pos[1] == (height + 2):
                world[pos] = 'o'
                units += 1
                pos = (500, 0)
                continue

        move = calculate_move(pos, new_pos, world)
        if not move:
            world[pos] = 'o'
            units += 1
            pos = (500, 0)
        else:
            pos = move

    return units


part1_world = copy.deepcopy(world)
print(simulate_sand(part1_world, height))


# Part 2
part2_world = copy.deepcopy(world)
print(simulate_sand(part2_world, height, True))
