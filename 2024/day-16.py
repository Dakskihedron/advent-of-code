from collections import defaultdict

# Part one
def lowest_maze_score(maze, start, end):

    def is_wall(y, x):
        return maze[y][x] == '#'

    d_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dist, prev, pq = {}, defaultdict(set), []

    prev[start] = None
    start = (*start, 1)
    dist[start] = 0
    pq.append(start)

    while len(pq) != 0:
        u = pq.pop(0)
        y, x, d = u

        dy, dx = d_offsets[d]

        # Going forwards
        if not is_wall(y+dy, x+dx):
            v = (y+dy, x+dx, d)
            cost = dist.get(u, float('inf'))
            alt = cost + 1
            if alt <= dist.get(v, float('inf')):
                dist[v] = alt
                if prev[(y+dy, x+dx)] != None:
                    prev[(y+dy, x+dx)].add((y, x, cost))
                pq.append(v)

        # Turning left
        lr = (d-1) % 4
        lry, lrx = d_offsets[lr]
        if not is_wall(y+lry, x+lrx):
            lrv = (y, x, lr)
            cost = dist.get(u, float('inf'))
            alt = cost + 1000
            if alt <= dist.get(lrv, float('inf')):
                dist[lrv] = alt
                if prev[(y, x)] != None:
                    prev[(y, x)].add((y, x, cost))
                pq.append(lrv)

        # Turning right
        rr = (d+1) % 4
        rry, rrx = d_offsets[rr]
        if not is_wall(y+rry, x+rrx):
            rrv = (y, x, rr)
            cost = dist.get(u, float('inf'))
            alt = cost + 1000
            if alt <= dist.get(rrv, float('inf')):
                dist[rrv] = alt
                if prev[(y, x)] != None:
                    prev[(y, x)].add((y, x, cost))
                pq.append(rrv)

    y, x = end
    final_scores = {}
    for k in dist.keys():
        if k[0] == y and k[1] == x:
            final_scores[k] = dist[k]

    min_score = min(final_scores.values())

    print('Part one:', min_score)
    return prev, min_score


# Part two
def count_tiles(prev, score, start, end):

    def traverse(u, score, seen=set()):
        if u in seen:
            return set()

        if u == start:
            return seen
        
        seen.add(u)
        n = prev[u]

        next = []
        for i in n:
            y, x, s = i
            if s == (score - 1):
                next.append(traverse((y, x), score-1, seen.copy()))
            elif s == (score - 1000):
                next.append(traverse((y, x), score-1000, seen.copy()))
            elif s == (score - 1001):
                next.append(traverse((y, x), score-1001, seen.copy()))

        return seen.union(*next)
    
    seen = traverse(end, score)
    print('Part two:', len(seen) + 1)


def main():
    with open('inputs/day-16.in', 'r') as file:
        maze = [[_ for _ in _] for _ in file.read().strip().split('\n')]

    start = (len(maze)-2, 1)
    end = (1, len(maze[0])-2)

    prev, score = lowest_maze_score(maze, start, end)
    count_tiles(prev, score, start, end)

if __name__ == '__main__':
    main()
