import heapq

with open('inputs/day-16.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [x.replace(',', '').replace(';', '').split(' ') for x in data]
    data = { x[1]: { 'rate': int(x[4][5:]), 'adj': x[9:] } for x in data }


# Part one
def dijkstra(data, src):
    dist = {}
    pq = []

    dist[src] = 0

    for v in data.keys():
        if v != src:
            dist[v] = float('inf')
        heapq.heappush(pq, (v, dist[v]))

    while len(pq) != 0:
        u = heapq.heappop(pq)[0]
        for v in data[u]['adj']:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (v, alt))

    return dist


def dfs(data, dist, src, time):
    paths = []

    def calc_paths(data, dist, src, time, visited):
        if time < 1:
            return

        for v, d in dist[src].items():
            if data[v]['rate'] == 0:
                continue

            if v in visited:
                continue

            if (time - d - 1) < 1:
                continue

            calc_paths(data, dist, v, time - d - 1, [*visited, v])
        paths.append(visited)

    calc_paths(data, dist, src, time, [])
    return paths


def calc_pres(data, dist, path, time):
    pressure = 0
    for v, w in zip(["AA", *path], path):
        time -= dist[v][w] + 1
        pressure += time * data[w]['rate']
    return pressure


dist = { valve: dijkstra(data, valve) for valve in data.keys() }
paths = dfs(data, dist, 'AA', 30)
print('Part 1:', max([calc_pres(data, dist, p, 30) for p in paths]))


# Part two (gives the right answer for my input, but not the example)
paths = dfs(data, dist, 'AA', 26)
pres_paths = { calc_pres(data, dist, p, 26): p for p in paths }
highest = 0
for k1, v1 in pres_paths.items():
    for k2, v2 in pres_paths.items():
        if len(set(v1).intersection(set(v2))) == 0:
            if (k1 + k2) > highest:
                highest = k1 + k2

print('Part 2:', highest)