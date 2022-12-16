with open('inputs/day-3.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = list(map(list, data))


# Part one
rugsacks = [[x[:len(x) // 2],x[len(x) // 2:]] for x in data]
answer = 0
for sack in rugsacks:
    item = list(set(sack[0]).intersection(set(sack[1])))[0]
    if item.isupper():
        answer += ord(item) - 38
    else:
        answer += ord(item) - 96
print('Part 1:', answer)


# Part two
groups = [data[i:i+3] for i in range(0, len(data), 3)]
answer = 0
for group in groups:
    item = list((set(group[0]).intersection(set(group[1])).intersection(set(group[2]))))[0]
    if item.isupper():
        answer += ord(item) - 38
    else:
        answer += ord(item) - 96
print('Part 2:', answer)