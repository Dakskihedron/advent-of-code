import heapq

with open('inputs/day-15.txt') as file:
    data = file.read().split('\n')
    data = [list(map(int, x)) for x in data]


# Part one
def get_adj(y, x, graph):
    adj = []
    if y > 0:
        adj.append((y-1, x))
    if y < len(graph) - 1:
        adj.append((y+1, x))
    if x > 0:
        adj.append((y, x-1))
    if x < len(graph[y]) - 1:
        adj.append((y, x+1))
    return adj

def dijkstra(source, target, graph):
    dist = {}
    prev = {}
    dist[source] = 0
    pq = []
    heapq.heapify(pq)

    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if (y, x) != source:
                dist[(y, x)] = float('inf')
                prev[(y, x)] = None
            heapq.heappush(pq, (dist[(y, x)], (y, x)))

    while len(pq) != 0:
        u = heapq.heappop(pq)[1]

        if u == target:
            risk = []
            u = target
            while u != source:
                risk.append(graph[u[0]][u[1]])
                u = prev[u]
            return sum(risk)

        for v in get_adj(u[0], u[1], graph):
            alt = dist[u] + graph[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    return dist, prev

print(dijkstra((0, 0), (len(data) - 1, len(data[0]) - 1), data))


# Part two
wrap = lambda n: (n % 9) + 1
data_5x = [[list(i) for i in data]]
data_5x_v2 = []

for _ in range(4):
    new_list = [list(map(wrap, i)) for i in data_5x[-1]]
    data_5x.append(new_list)
for i in range(len(data_5x)):
    for j in range(len(data_5x[i])):
        data_5x_v2.append(data_5x[i][j])

for row in range(len(data_5x_v2)):
    new_row = [list(i for i in data_5x_v2[row])]
    for _ in range(4):
        x = list(map(wrap, new_row[-1]))
        new_row.append(x)
    flatten = []
    for x in new_row:
        for y in x:
            flatten.append(y)
    data_5x_v2[row] = flatten

print(dijkstra((0, 0), (len(data_5x_v2) - 1, len(data_5x_v2[0]) - 1), data_5x_v2))