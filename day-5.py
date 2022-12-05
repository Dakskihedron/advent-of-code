with open('inputs/day-5.txt', 'r') as file:
    stacks, data = file.read().strip().split('\n\n')
    data = data.split('\n')

# Part one
stacks_original = [
    "WTHPJCF",
    "HBJZFVRG",
    "RTPH",
    "THPNSZ",
    "DCJHZFVN",
    "ZDWFGMP",
    "PDJSWZVM",
    "SDN",
    "MFSZD"
]

stacks = [x for x in stacks_original]

for line in data:
    move = line.split(' ')
    num, start, end = int(move[1]), int(move[3]), int(move[5])
    crates = stacks[start-1][0:num][::-1]
    stacks[start-1] = stacks[start-1][num:]
    stacks[end-1] = crates + stacks[end-1]

print(''.join([x[0] for x in stacks]))

# Part two
stacks = [x for x in stacks_original]

for line in data:
    move = line.split(' ')
    num, start, end = int(move[1]), int(move[3]), int(move[5])
    crates = stacks[start-1][0:num]
    stacks[start-1] = stacks[start-1][num:]
    stacks[end-1] = crates + stacks[end-1]

print(''.join([x[0] for x in stacks]))