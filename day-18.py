import copy
import heapq

with open('inputs/day-18.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [tuple(map(int, x.split(','))) for x in data]


# Part one
world_origin = {}
for c in data:
    world_origin.setdefault(c, [])

def calc_surface_area(world, data):
    for c in data:
        x1, y1, z1 = c
        for k in world.keys():
            x2, y2, z2 = k
            if (x1 + 1 == x2 or x1 - 1 == x2) and (y1 == y2 and z1 == z2):
                world[k].append(c)
            if (y1 + 1 == y2 or y1 - 1 == y2) and (x1 == x2 and z1 == z2):
                world[k].append(c)
            if (z1 + 1 == z2 or z1 - 1 == z2) and (x1 == x2 and y1 == y2):
                world[k].append(c)

    return sum(map(lambda x: 6 - len(x), world.values()))

world = copy.deepcopy(world_origin)
surface_area = calc_surface_area(world, data)
print('Part 1:', surface_area)


# Part two

# 3D floodfill algorithm
def floodfill3d(start, end, world):
    sx, sy, sz = start
    ex, ey, ez = end
    seen = set()
    q = []
    heapq.heappush(q, start)

    while len(q) != 0:
        n = heapq.heappop(q)
        if n not in seen and n not in world:
            seen.add(n)
            x, y, z = n

            # x values
            if x+1 <= ex:
                heapq.heappush(q, (x+1, y, z))
            if x-1 >= sx:
                heapq.heappush(q, (x-1, y, z))

            # y values
            if y+1 <= ey:
                heapq.heappush(q, (x, y+1, z))
            if y-1 >= sy:
                heapq.heappush(q, (x, y-1, z))

            # z values
            if z+1 <= ez:
                heapq.heappush(q, (x, y, z+1))
            if z-1 >= sz:
                heapq.heappush(q, (x, y, z-1))

    return seen


# Define min and max x y z
min_x, min_y, min_z = 0, 0, 0
max_x, max_y, max_z = 0, 0, 0
for c in data:
    x, y, z = c
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if z > max_z:
        max_z = z


# Calc interior surface area
seen = floodfill3d((min_x, min_y, min_z), (max_x, max_y, max_z), world_origin)

interior = []
interior_world = {}
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        for z in range(min_z, max_z + 1):
            if (x, y, z) not in seen and (x, y, z) not in world_origin:
                interior.append((x, y, z))
                interior_world.setdefault((x, y, z), [])

interior_sa = calc_surface_area(interior_world, interior)

print('Part 2:', surface_area - interior_sa)