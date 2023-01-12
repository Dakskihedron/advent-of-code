with open('inputs/day-22.txt', 'r') as file:
    board, data = file.read().split('\n\n')
    board = [[_ for _ in _] for _ in board.split('\n')]
    data = data.strip()


# Part 1
def fnd_passwd(world, data):
    ir = 0
    bearing = 0
    pos = list(world.keys())[0]

    while not ir >= len(data):
        if data[ir].isdigit():
            if len(data) > ir+1 and data[ir+1].isdigit():
                ir_incr = 2
                move = int(data[ir:ir+2])
            else:
                ir_incr = 1
                move = int(data[ir])
        else:
            move = data[ir]
            ir_incr = 1
            if move == 'L':
                bearing = (bearing - 1) % 4
            else:
                bearing = (bearing + 1) % 4
            ir += ir_incr
            continue


        for _ in range(move):
            x, y = pos
            if bearing == 0:
                new_pos = (x+1, y)
            elif bearing == 1:
                new_pos = (x, y+1)
            elif bearing == 2:
                new_pos = (x-1, y)
            else:
                new_pos = (x, y-1)


            tile = world.get(new_pos, None)
            if tile == '#':
                break
            elif tile == '.':
                pos = new_pos
            else:
                x, y = pos
                if bearing == 0 or bearing == 2:
                    x_vals = [_[0] for _ in world.keys() if _[1] == y]
                    i = x_vals.index(x)
                    off = 1 if bearing == 0 else -1
                    new_x = x_vals[(i+off) % len(x_vals)]
                    if world.get((new_x, y)) != '#':
                        pos = (new_x, y)
                else:
                    y_vals = [_[1] for _ in world.keys() if _[0] == x]
                    i = y_vals.index(y)
                    off = 1 if bearing == 1 else -1
                    new_y = y_vals[(i+off) % len(y_vals)]
                    if world.get((x, new_y)) != '#':
                        pos = (x, new_y)
        
        ir += ir_incr
    return (1000 * (y+1)) + (4 * (x+1)) + bearing


world = {}
for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x] != ' ':
            world[(x,y)] = board[y][x]

print('Part 1:', fnd_passwd(world, data))


# Part 2
with open('inputs/day-22b.txt', 'r') as file:
    board = file.read().split('\n\n')
    board = [[[_ for _ in _] for _ in _.split('\n')] for _ in board]

# day-22b.txt consists only of the faces in following format:
# 111
# 111
# 111
#
# 222
# 222
# 222
#
# 333
# 333
# 333
#
# 444
# 444
# 444
#
# 555
# 555
# 555
#
# 666
# 666
# 666


def fnd_passwd_cube(world, data):
    face = 'A'
    ir = 0
    bearing = 0
    pos = (0,0)

    while not ir >= len(data):
        if data[ir].isdigit():
            if len(data) > ir+1 and data[ir+1].isdigit():
                ir_incr = 2
                move = int(data[ir:ir+2])
            else:
                ir_incr = 1
                move = int(data[ir])
        else:
            move = data[ir]
            ir_incr = 1
            if move == 'L':
                bearing = (bearing - 1) % 4
            else:
                bearing = (bearing + 1) % 4
            ir += ir_incr
            continue

        for _ in range(move):
            x, y = pos
            if bearing == 0:
                new_pos = (x+1, y)
            elif bearing == 1:
                new_pos = (x, y+1)
            elif bearing == 2:
                new_pos = (x-1, y)
            else:
                new_pos = (x, y-1)

            def _try_move(world, new_pos, new_bearing, next_face):
                nonlocal pos, bearing, face
                if world[next_face].get(new_pos, None) == '.':
                    pos = new_pos
                    bearing = new_bearing
                    face = next_face
                    return True
                return False

            new_x, new_y = new_pos

            # All translation values are hardcoded to work with my input

            # Translate to left face
            if new_x < 0:
                if face == 'A':
                    if not _try_move(world, (0, ((-1 * new_y) % 50) - 1 if new_y != 0 else 49), 0, 'D'):
                        break
                elif face == 'B':
                    if not _try_move(world, (49, new_y), bearing, 'A'):
                        break
                elif face == 'C':
                    if not _try_move(world, (new_y, 0), 1, 'D'):
                        break
                elif face == 'D':
                    if not _try_move(world, (0, ((-1 * new_y) % 50) - 1 if new_y != 0 else 49), 0, 'A'):
                        break
                elif face == 'E':
                    if not _try_move(world, (49, new_y), bearing, 'D'):
                        break
                elif face == 'F':
                    if not _try_move(world, (new_y, 0), 1, 'A'):
                        break

            # Translate to right face
            elif new_x > 49:
                if face == 'A':
                    if not _try_move(world, (0, new_y), bearing, 'B'):
                        break
                elif face == 'B':
                    if not _try_move(world, (49, ((-1 * new_y) % 50) - 1 if new_y != 0 else 49), 2, 'E'):
                        break
                elif face == 'C':
                    if not _try_move(world, (new_y, 49), 3, 'B'):
                        break
                elif face == 'D':
                    if not _try_move(world, (0, new_y), bearing, 'E'):
                        break
                elif face == 'E':
                    if not _try_move(world, (49, ((-1 * new_y) % 50) - 1 if new_y != 0 else 49), 2, 'B'):
                        break
                elif face == 'F':
                    if not _try_move(world, (new_y, 49), 3, 'E'):
                        break

            # Translate to face above
            elif new_y < 0:
                if face == 'A':
                    if not _try_move(world, (0, new_x), 0, 'F'):
                        break
                elif face == 'B':
                    if not _try_move(world, (new_x, 49), bearing, 'F'):
                        break
                elif face == 'C':
                    if not _try_move(world, (new_x, 49), bearing, 'A'):
                        break
                elif face == 'D':
                    if not _try_move(world, (0, new_x), 0, 'C'):
                        break
                elif face == 'E':
                    if not _try_move(world, (new_x, 49), bearing, 'C'):
                        break
                elif face == 'F':
                    if not _try_move(world, (new_x, 49), bearing, 'D'):
                        break

            # Translate to face below
            elif new_y > 49:
                if face == 'A':
                    if not _try_move(world, (new_x, 0), bearing, 'C'):
                        break
                elif face == 'B':
                    if not _try_move(world, (49, new_x), 2, 'C'):
                        break
                elif face == 'C':
                    if not _try_move(world, (new_x, 0), bearing, 'E'):
                        break
                elif face == 'D':
                    if not _try_move(world, (new_x, 0), bearing, 'F'):
                        break
                elif face == 'E':
                    if not _try_move(world, (49, new_x), 2, 'F'):
                        break
                elif face == 'F':
                    if not _try_move(world, (new_x, 0), bearing, 'B'):
                        break
            else:
                if not _try_move(world, new_pos, bearing, face):
                    break

        ir += ir_incr

    return pos, bearing, face


cube = {}
face = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(len(face)):
    cube[face[i]] = {}
    for y in range(len(board[i])):
        for x in range(len(board[i][y])):
            cube[face[i]][(x,y)] = board[i][y][x]

pos, bearing, face = fnd_passwd_cube(cube, data)
x, y = pos
x += 1
y += 1

if face == 'A':
    x += 50
elif face == 'B':
    x += 100
elif face == 'C':
    x += 50
    y += 50
elif face == 'D':
    y += 100
elif face == 'E':
    x += 50
    y += 100
elif face == 'F':
    y += 150

passwd = (1000 * y) + (4 * x) + bearing
print('Part 2:', passwd)