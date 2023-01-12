from collections import defaultdict

with open('inputs/day-12.txt') as file:
    data = file.read().split('\n')
    data = [x.split('-') for x in data]

graph = defaultdict(set)
for v1, v2 in data:
    graph[v1].add(v2)
    graph[v2].add(v1)

# Part one
def dfs(path=['start']):
    if path[-1] == 'end':
        return 1
    new_paths = [x for x in graph[path[-1]] if x not in path or x.isupper()]
    if len(new_paths) == 0:
        return 0
    return sum([dfs(path=path+[x]) for x in new_paths])

print(dfs())

# Part two
def no_dupes(path):
    for x in path:
        if x.islower():
            if path.count(x) > 1:
                return False
    return True

def dfs(path=['start']):
    if path[-1] == 'end':
        return 1
    new_paths = []
    for x in graph[path[-1]]:
        if x.islower() and x in path and x != 'start':
            if no_dupes(path):
                new_paths.append(x)
        if x not in path or x.isupper():
            new_paths.append(x)
    if len(new_paths) == 0:
        return 0
    return sum([dfs(path=path+[x]) for x in new_paths])

print(dfs())