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
# def floodfill(data, start, og_seen):
#     edge = False
#     seen = set()
#     q = []
#     heapq.heappush(q, start)

#     while len(q) != 0:
#         n = heapq.heappop(q)
#         ny, nx = n
#         if data[ny][nx] in ['.', 'J', '|', 'L', 'F', '7', '-'] and n not in seen and n not in og_seen:
#             if ny == 0 or ny == len(data)-1 or nx == 0 or nx == len(data[0])-1:
#                 edge = True
#             seen.add(n)

#             if ny > 0:
#                 heapq.heappush(q, (ny-1,nx))
#             if ny < len(data)-1:
#                 heapq.heappush(q, (ny+1,nx))
#             if nx > 0:
#                 heapq.heappush(q, (ny,nx-1))
#             if nx < len(data[0])-1:
#                 heapq.heappush(q, (ny,nx+1))

#     return seen, edge


# def get_enclosed_count(data, loop_count, seen):
#     not_enclosed = 0

#     for y in range(len(data)):
#         for x in range(len(data[y])):
#             if (y,x) not in seen:
#                 if data[y][x] in ['.', 'J', '|', 'L', 'F', '7', '-']:
#                     new_seen, edge = floodfill(data, (y,x), seen)
#                     if edge:
#                         not_enclosed += len(new_seen)
#                     seen = seen.union(new_seen)
#                 elif y == 0 or y == len(data)-1 or x == 0 or x == len(data[0])-1:
#                     not_enclosed += 1

#     final = (len(data) * len(data[0])) - (loop_count * 2) - not_enclosed
#     print('Part two:', final)


def get_enclosed_count(data, start, loop_seen):
    enclosed = set()
    seen = set()
    dir = None
    orient = None
    cur = None

    new_dir = {
        'up': {'|': 'up', '7': 'left', 'F': 'right'},
        'down': {'|': 'down', 'J': 'left', 'L': 'right'},
        'left': {'-': 'left', 'L': 'up', 'F': 'down'},
        'right': {'-': 'right', 'J': 'up', '7': 'down'}
    }

    new_orient = {
        'up': 0, 'right': 1, ''
    }


    sy, sx = start
    if sy > 0 and data[sy-1][sx] in ['|', 'F', '7']:
        cur = (sy-1, sx)
        dir = 'up'
        orient = 0
    elif sy < len(data)-1 and data[sy+1][sx] in ['|', 'L', 'J']:
        cur = (sy+1, sx)
        dir = 'down'
        orient = 0
    elif sx > 0 and data[sy][sx-1] in ['-', 'L', 'F']:
        cur = (sy, sx-1)
        dir = 'left'
        orient = 1
    elif sx < len(data[0])-1 and data[sy][sx+1] in ['-', 'J', '7']:
        cur = (sy, sx+1)
        dir = 'right'
        orient = 1

    while True:
        y, x = cur
        seen.add(cur)

        if dir == 'up':
            cur = (y-1,x)
        elif dir == 'down':
            cur = (y+1,x)
        elif dir == 'left':
            cur = (y,x-1)
        else:
            cur = (y,x+1)
        
        ny,nx = cur

        if (ny,nx) == start:
            break

        p_next = data[ny][nx]
        old_dir = dir
        dir = new_dir[old_dir][p_next]
        



    print()


def main():
    with open('inputs/test.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [[_ for _ in _] for _ in data]
        sy, sx = list(zip(*np.where(np.array([[_ for _ in _] for _ in data]) == 'S')))[0]

    steps, seen = get_furthest_steps(data, (sy, sx))
    print('Part one:', steps)
    get_enclosed_count(data, steps, seen)


if __name__ == '__main__':
    main()