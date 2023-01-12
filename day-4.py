with open('inputs/day-4.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [[y.split('-') for y in x.split(',')] for x in data]


# Part one
answer = 0
for pair in data:
    if (int(pair[0][0]) >= int(pair[1][0])) and (int(pair[0][1]) <= int(pair[1][1])):
        answer += 1
    elif (int(pair[0][0]) <= int(pair[1][0])) and (int(pair[0][1]) >= int(pair[1][1])):
        answer += 1
print('Part 1:', answer)


# Part two
answer = 0
for pair in data:
    elf1 = set(range(int(pair[0][0]), int(pair[0][1]) + 1))
    elf2 = set(range(int(pair[1][0]), int(pair[1][1]) + 1))
    if len(elf1.intersection(elf2)) != 0:
        answer += 1
print('Part 2:', answer)
