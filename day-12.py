import heapq

with open('inputs/day-12.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [[y for y in x] for x in data]


# Part one
class Graph:
    def __init__(self):
        self.__vertices = {}

    def add_vertex(self, vertex):
        self.__vertices[vertex] = []

    def add_adj(self, vertex, adj):
        self.__vertices[vertex] += adj

    def vertices(self):
        return self.__vertices.keys()

    def get_adj(self, vertex):
        return self.__vertices[vertex]

    def remove(self, vertex, value):
        self.__vertices[vertex].remove(value)

    def __str__(self):
        return str(self.__vertices)


def dijkstra(graph: Graph, src, dest):
    dist = {}
    pq = []

    dist[src] = 0

    for v in graph.vertices():
        if v != src:
            dist[v] = float('inf')
        heapq.heappush(pq, (v, dist[v]))

    while len(pq) != 0:
        u = heapq.heappop(pq)[0]
        for v in graph.get_adj(u):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (v, alt))
    return dist[dest]


def get_adj(y, x, data):
    if data[y][x] == 'S':
        src = ord('a')
    elif data[y][x] == 'E':
        src = ord('z')
    else:
        src = ord(data[y][x])

    adj = []
    if y > 0:
        if ord(data[y-1][x]) <= (src + 1):
            adj.append((y-1,x))
    if y < len(data) - 1:
        if ord(data[y+1][x]) <= (src + 1):
            adj.append((y+1,x))
    if x > 0:
        if ord(data[y][x-1]) <= (src + 1):
            adj.append((y,x-1))
    if x < len(data[y]) - 1:
        if ord(data[y][x+1]) <= (src + 1):
            adj.append((y,x+1))
    return adj


graph = Graph()

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'S':
            src = (y,x)
        if data[y][x] == 'E':
            dest = (y,x)
        graph.add_vertex((y,x))
        graph.add_adj((y,x), get_adj(y, x, data))

# For some unknown reason, the dest gets added to all of its surrounding vertices
# so we have to remove it from those which are not 'z'
for v in graph.vertices():
    if dest in graph.get_adj(v):
        if data[v[0]][v[1]] != 'z':
            graph.remove(v, dest)

print('Part 1:', dijkstra(graph, src, dest))


# Part two
# Nasty and unoptimised, but its 4am
a_coords = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'a':
            a_coords.append((y,x))

distances = []
for src in a_coords:
    distances.append(dijkstra(graph, src, dest))
print('Part 2:', min(distances))