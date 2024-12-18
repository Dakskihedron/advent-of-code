# Part one
def dijkstra(start, space, max_x, max_y):
    dist = {}
    dist[start] = 0
    pq = []
    pq.append(start)

    while len(pq) != 0:
        u = pq.pop(0)
        x, y = u

        adj = []
        if y-1 >= 0:
            adj.append((x, y-1))
        if y+1 < max_y+1:
            adj.append((x, y+1))
        if x-1 >= 0:
            adj.append((x-1, y))
        if x+1 < max_x+1:
            adj.append((x+1, y))

        for n in adj:
            x, y = n
            if space[y][x] == '.':
                alt = dist.get(u, float('inf')) + 1
                if alt < dist.get(n, float('inf')):
                    dist[n] = alt
                    pq.append(n)

    return dist


def minimum_steps(data):
    max_x, max_y = 70, 70
    start, end = (0, 0), (max_x, max_y)
    space = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]

    for i in range(1024):
        x, y = data[i]
        space[y][x] = '#'

    dist = dijkstra(start, space, max_x, max_y)

    print('Part one:', dist[end])


# Part two
def first_cutoff_byte_coord(data):
    max_x, max_y = 70, 70
    start, end = (0, 0), (max_x, max_y)
    space = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]

    for i in range(1024):
        x, y = data[i]
        space[y][x] = '#'

    for i in range(1025, len(data)):
        x, y = data[i]
        space[y][x] = '#'

        dist = dijkstra(start, space, max_x, max_y)
        if end not in dist:
            print(f'Part two: {x},{y}')
            break


def main():
    with open('inputs/day-18.in', 'r') as file:
        data = [_.split(',') for _ in file.read().strip().split('\n')]
        data = [(int(_[0]), int(_[1])) for _ in data]

    minimum_steps(data)
    first_cutoff_byte_coord(data)

if __name__ == '__main__':
    main()
