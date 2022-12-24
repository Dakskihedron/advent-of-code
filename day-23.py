from collections import defaultdict
import copy

with open('inputs/day-23.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [[_ for _ in _] for _ in data]


# Part one
def init_world(data):
    world = {}
    elf = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                world[(x,y)] = elf
                elf += 1
    return world, elf


def sim_planting(world, elf_count, rounds, get_rounds=False):
    compass = [0, 1, 2, 3]

    if get_rounds:
        curr_copy = copy.deepcopy(world)

    for n in range(rounds):
        world_new = defaultdict(list)

        for i in world.items():
            pos, elf = i
            x, y = pos

            adj = list(map(lambda p: p in world.keys(), [(x,y-1), (x-1,y-1), (x+1,y-1), (x,y+1), (x-1,y+1), (x+1,y+1), (x-1,y), (x+1,y)]))
            if sum(adj) == 0:
                continue

            for d in compass:
                if d == 0 and world.get((x,y-1), None) == None and world.get((x-1,y-1), None) == None and world.get((x+1,y-1), None) == None:
                    world_new[(x,y-1)].append((elf, pos))
                    break

                elif d == 1 and world.get((x,y+1), None) == None and world.get((x-1,y+1), None) == None and world.get((x+1,y+1), None) == None:
                    world_new[(x,y+1)].append((elf, pos))
                    break

                elif d == 2 and world.get((x-1,y), None) == None and world.get((x-1,y-1), None) == None and world.get((x-1,y+1), None) == None:
                    world_new[(x-1,y)].append((elf, pos))
                    break

                elif d == 3 and world.get((x+1,y), None) == None and world.get((x+1,y-1), None) == None and world.get((x+1,y+1), None) == None:
                    world_new[(x+1,y)].append((elf, pos))
                    break
        
        compass.append(compass.pop(0))

        for k,v in world_new.items():
            if len(v) == 1:
                elf, pos = v[0]
                world.pop(pos)
                world[k] = elf

        if get_rounds:
            if world == curr_copy:
                return n + 1
            else:
                curr_copy = copy.deepcopy(world)

    if not get_rounds:
        x_vals = [v[0] for v in world.keys()]
        y_vals = [v[1] for v in world.keys()]
        x_len = (max(x_vals) - min(x_vals)) + 1
        y_len = (max(y_vals) - min(y_vals)) + 1
        return (y_len * x_len) - elf_count
    else:
        return "Not enough rounds."


world, elf_count = init_world(data)
print('Part 1:', sim_planting(world, elf_count, 10))


# Part two
world, elf_count = init_world(data)
print('Part 2:', sim_planting(world, elf_count, 10000, True))