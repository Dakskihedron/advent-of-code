with open('inputs/day-17.txt', 'r') as file:
    data = [x for x in file.read().strip()]


# Part one
def simulate_rockfall(data, world, units, logging=False):
    fallen_count = 0
    curr_height = 0

    # Rock types
    rock_types = {
        0: [(0,0), (1,0), (2,0), (3,0)],
        1: [(1,0), (0,1), (1,1), (2,1), (1,2)],
        2: [(0,0), (1,0), (2,0), (2,1), (2,2)],
        3: [(0,0), (0,1), (0,2), (0,3)],
        4: [(0,0), (1,0), (0,1), (1,1)]
    }

    curr_rock_type = 0
    curr_rock_pos = [p for p in rock_types[curr_rock_type]]

    ir = 0

    # Init starting rock
    for pos in range(len(curr_rock_pos)):
        x, y = curr_rock_pos[pos]
        x += 2
        y += 3
        curr_rock_pos[pos] = (x,y)

    cycles = {}

    while fallen_count != units:
        if ir == 0:
            if curr_rock_type in cycles:
                cycles[curr_rock_type] += [(fallen_count, curr_height)]
            else:
                cycles[curr_rock_type] = [(fallen_count, curr_height)]

            # Print last 50 positions and current rock shape positions
            if logging:
                keys = [k for k in list(world.keys())[-50:]]
                world_logging = { k: '#' for k in keys }
                print('World (last 50):', world_logging, '\n')
                print('Rock pos:', curr_rock_pos, '\n')

        move = data[ir]
        if move == '<':
            offset = -1
        else:
            offset = 1

        # Calc if left/right movement is valid
        can_move = True
        new_rock_pos = [p for p in curr_rock_pos]
        for pos in range(len(new_rock_pos)):
            x, y = new_rock_pos[pos]
            if (x + offset == -1) or (x + offset == 7) or world.get((x + offset, y), '.') == '#':
                can_move = False
                break
            else:
                new_rock_pos[pos] = (x + offset, y)

        if can_move:
            curr_rock_pos = [p for p in new_rock_pos]

        # If downwards movement is valid
        can_move = True
        new_rock_pos = [p for p in curr_rock_pos]
        for pos in range(len(new_rock_pos)):
            x, y = new_rock_pos[pos]
            if (y - 1 == -1) or world.get((x, y - 1), '.') == '#':
                can_move = False
                break
            else:
                new_rock_pos[pos] = (x, y - 1)

        if can_move:
            curr_rock_pos = [p for p in new_rock_pos]
        else:
            # End current rock
            for pos in curr_rock_pos:
                world.setdefault(pos, '#')
                _, y = pos
                if (y + 1) > curr_height:
                    curr_height = y + 1

            # Setup next rock
            fallen_count += 1
            curr_rock_type = (curr_rock_type + 1) % len(rock_types.keys())
            curr_rock_pos = [p for p in rock_types[curr_rock_type]]
            for pos in range(len(curr_rock_pos)):
                x, y = curr_rock_pos[pos]
                x += 2
                y += curr_height + 3
                curr_rock_pos[pos] = (x,y)
        
        ir = (ir + 1) % len(data)

    return curr_height, cycles

world = {}
height, _ = simulate_rockfall(data, world, 2022)
print('Part 1:', height)


# Part two
TODO