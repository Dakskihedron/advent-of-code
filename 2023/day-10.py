from collections import defaultdict
import numpy as np
import heapq
import time


# Part one
def get_next(data, pos):
    y, x = pos
    pipe = data[y][x]
    if pipe == '|':
        return (y-1,x), (y+1,x)
    if pipe == 'F':
        return (y,x+1), (y+1,x)
    if pipe == '7':
        return (y,x-1), (y+1,x)
    if pipe == 'L':
        return (y-1,x), (y,x+1)
    if pipe == 'J':
        return (y-1,x), (y,x-1)
    if pipe == '-':
        return (y,x-1), (y,x+1)


def get_furthest_steps(data, start):
    q = []
    seen = set()
    steps = 1
    seen.add(start)

    sy, sx = start
    if sy > 0 and data[sy-1][sx] in ['|', 'F', '7']:
        heapq.heappush(q, (sy-1, sx))
    if sy < len(data)-1 and data[sy+1][sx] in ['|', 'L', 'J']:
        heapq.heappush(q, (sy+1, sx))
    if sx > 0 and data[sy][sx-1] in ['-', 'L', 'F']:
        heapq.heappush(q, (sy, sx-1))
    if sx < len(data[0])-1 and data[sy][sx+1] in ['-', 'J', '7']:
        heapq.heappush(q, (sy, sx+1))

    while True:
        m = heapq.heappop(q)
        seen.add(m)
        m1, m2 = get_next(data, m)
        m_next = m1 if m2 in seen else m2

        n = heapq.heappop(q)
        seen.add(n)
        n1, n2 = get_next(data, n)
        n_next = n1 if n2 in seen else n2

        steps += 1

        if m_next == n_next:
            seen.add(m_next)
            break

        heapq.heappush(q, m_next)
        heapq.heappush(q, n_next)

    return steps, seen


# Part two
def floodfill(data, start, og_seen):
    q = []
    seen = set()
    heapq.heappush(q, start)

    while len(q) != 0:
        n = heapq.heappop(q)
        ny, nx = n
        if data[ny][nx] in ['.', 'J', '|', 'L', 'F', '7', '-'] and n not in seen and n not in og_seen:
            seen.add(n)

            if ny > 0:
                heapq.heappush(q, (ny-1,nx))
            if ny < len(data)-1:
                heapq.heappush(q, (ny+1,nx))
            if nx > 0:
                heapq.heappush(q, (ny,nx-1))
            if nx < len(data[0])-1:
                heapq.heappush(q, (ny,nx+1))

    return seen


def get_enclosed_count(data, start, loop_seen):
    enclosed = set()
    dir = None
    cur = None

    next_dir = {
        'up': {'|': 'up', '7': 'left', 'F': 'right'},
        'down': {'|': 'down', 'J': 'left', 'L': 'right'},
        'left': {'-': 'left', 'L': 'up', 'F': 'down'},
        'right': {'-': 'right', 'J': 'up', '7': 'down'}
    }

    sy, sx = start
    n, e, s, w = False, False, False, False
    if sy > 0 and data[sy-1][sx] in ['|', 'F', '7']:
        n = True
    if sy < len(data)-1 and data[sy+1][sx] in ['|', 'L', 'J']:
        s = True
    if sx > 0 and data[sy][sx-1] in ['-', 'L', 'F']:
        w = True
    if sx < len(data[0])-1 and data[sy][sx+1] in ['-', 'J', '7']:
        e = True

    starting = {
        (True, False, False, True): ('up', (sy-1,sx)),
        (False, True, False, True): ('right', (sy,sx+1)),
        (False, False, True, True): ('down', (sy+1,sx)),
        (False, True, True, False): ('right', (sy,sx+1)),
        (True, False, True, False): ('up', (sy-1,sx)),
        (True, True, False, False): ('right', (sy,sx+1))
    }

    dir, cur = starting[(n,e,s,w)]

    while True:
        y, x = cur
        p_cur = data[y][x]
        dir = next_dir[dir][p_cur]

        if dir == 'up':
            cur = (y-1,x)
            if x < len(data)-1 and (y,x+1) not in loop_seen:
                enclosed.add((y,x+1))
        elif dir == 'down':
            cur = (y+1,x)
            if x > 0 and (y,x-1) not in loop_seen:
                enclosed.add((y,x-1))
        elif dir == 'left':
            cur = (y,x-1)
            if y > 0 and (y-1,x) not in loop_seen:
                enclosed.add((y-1,x))
        elif dir == 'right':
            cur = (y,x+1)
            if y < len(data[0])-1 and (y+1,x) not in loop_seen:
                enclosed.add((y+1,x))

        ny,nx = cur

        if (ny,nx) == start:
            break

    flood_seen = set()
    for item in enclosed:
        if item not in flood_seen:
            flooded = floodfill(data, item, loop_seen)
            flood_seen = flood_seen.union(flooded)

    print('Part two:', len(flood_seen))


def main():
    with open('inputs/day-10.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [[_ for _ in _] for _ in data]
        sy, sx = list(zip(*np.where(np.array([[_ for _ in _] for _ in data]) == 'S')))[0]

    steps, seen = get_furthest_steps(data, (sy, sx))
    print('Part one:', steps)
    get_enclosed_count(data, (sy, sx), seen)


if __name__ == '__main__':
    main()