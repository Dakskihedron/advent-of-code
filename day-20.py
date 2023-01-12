with open('inputs/day-20.txt', 'r') as file:
    data = list(map(int, file.read().strip().split('\n')))


# Part one
def mix(mappings, datafile):
    for i in range(len(mappings.keys())):

        shift = mappings[i]
        index = datafile.index(i)

        new_index = (index + shift) % (len(datafile) - 1)

        val = datafile.pop(index)
        datafile.insert(new_index, val)
    return datafile


mappings = { _:data[_] for _ in range(len(data)) }

datafile = list(map(lambda i: mappings[i], mix(mappings, [*range(0, len(mappings.keys()))])))
answer = sum(map(lambda x: datafile[(datafile.index(0) + x) % len(datafile)], [1000, 2000, 3000]))
print('Part 1:', answer)


# Part two
mappings = { _:v * 811589153 for _,v in mappings.items() }
datafile = [*range(0, len(mappings.keys()))]

for _ in range(10):
    datafile = mix(mappings, datafile)

datafile = list(map(lambda i: mappings[i], datafile))
answer = sum(map(lambda x: datafile[(datafile.index(0) + x) % len(datafile)], [1000, 2000, 3000]))
print('Part 2:', answer)