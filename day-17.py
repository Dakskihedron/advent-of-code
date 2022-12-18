with open('inputs/day-17.txt', 'r') as file:
    data = [x for x in file.read().strip()]


# Part one
def simulate_rockfall(data, world, target):
    rocks = {
        0: [(0,0), (1,0), (2,0), (3,0)],
        1: [(1,0), (0,1), (1,1), (2,1), (1,2)],
        2: [(0,0), (1,0), (2,0), (2,1), (2,2)],
        3: [(0,0), (0,1), (0,2), (0,3)],
        4: [(0,0), (1,0), (0,1), (1,1)]
    }

    # Rocks fallen and height
    fallen = 0
    height = 0

    # Current rock type and positions
    rock_type = 0
    rock_pos = [_ for _ in rocks[rock_type]]

    # Initial rock position
    rock_pos = [(x+2,y+3) for x,y in rock_pos]

    # Current instruction
    ir = 0


    # Main loop
    while fallen != target:

        # Get current move and determine offset
        move = data[ir]
        if move == '<':
            offset = -1
        else:
            offset = 1


        # Calc left/right movement
        allowed = True
        new_rock_pos = [_ for _ in rock_pos]
        for p in range(len(new_rock_pos)):
            x, y = new_rock_pos[p]
            if (x+offset == -1) or (x+offset == 7) or world.get((x+offset, y), '.') == '#':
                allowed = False
                break
            else:
                new_rock_pos[p] = (x+offset, y)

        if allowed:
            rock_pos = [_ for _ in new_rock_pos]

        # Calc downwards movement
        allowed = True
        new_rock_pos = [_ for _ in rock_pos]
        for p in range(len(new_rock_pos)):
            x, y = new_rock_pos[p]
            if (y-1 == -1) or world.get((x, y-1), '.') == '#':
                allowed = False
                break
            else:
                new_rock_pos[p] = (x, y-1)
        
        if allowed:
            rock_pos = [_ for _ in new_rock_pos]

        # Downwards movement execution
        if allowed:
            rock_pos = [_ for _ in new_rock_pos]
        else:

            # Rock movement ceased
            for p in rock_pos:
                world.setdefault(p, '#')
                if (p[1] + 1) > height:
                    height = p[1] + 1

            # Next rock and instruction
            fallen += 1
            rock_type = (rock_type + 1) % len(rocks.keys())
            rock_pos = [_ for _ in rocks[rock_type]]
            rock_pos = [(x+2,y+height+3) for x,y in rock_pos]
        
        ir = (ir + 1) % len(data)

    return height

world = {}
height = simulate_rockfall(data, world, 2022)
print('Part 1:', height)


# Part two