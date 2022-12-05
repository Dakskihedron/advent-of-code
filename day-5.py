with open('inputs/day-5.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = data[10:]

# Part one
stacks_original = [
    ["W", "T", "H", "P", "J", "C", "F"],
    ["H", "B", "J", "Z", "F", "V", "R", "G"],
    ["R", "T", "P", "H"],
    ["T", "H", "P", "N", "S", "Z"],
    ["D", "C", "J", "H", "Z", "F", "V", "N"],
    ["Z", "D", "W", "F", "G", "M", "P"],
    ["P", "D", "J", "S", "W", "Z", "V", "M"],
    ["S", "D", "N"],
    ["M", "F", "S", "Z", "D"]
]

stacks = [x for x in stacks_original]

for line in data:
    move = line.split(' ')
    num = int(move[1])
    start = int(move[3])
    end = int(move[5])
    crates = stacks[start-1][0:num]
    crates.reverse()
    stacks[start-1] = stacks[start-1][num:]
    stacks[end-1] = crates + stacks[end-1]

print(''.join([x[0] for x in stacks]))

# Part two
stacks = [x for x in stacks_original]

for line in data:
    move = line.split(' ')
    num = int(move[1])
    start = int(move[3])
    end = int(move[5])
    crates = stacks[start-1][0:num]
    stacks[start-1] = stacks[start-1][num:]
    stacks[end-1] = crates + stacks[end-1]

print(''.join([x[0] for x in stacks]))