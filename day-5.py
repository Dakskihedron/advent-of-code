with open('inputs/day-5.txt', 'r') as file:
    stacks, data = file.read().strip().split('\n\n')
    data = data.split('\n')


# Part one
stacks = [
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

def move_crates(stacks, data, multi=False):
    new_stacks = [x for x in stacks]
    for line in data:
        move = line.split(' ')
        num, start, end = int(move[1]), int(move[3]), int(move[5])
        crates = new_stacks[start-1][0:num]
        if not multi:
            crates = crates[::-1]
        new_stacks[start-1] = new_stacks[start-1][num:]
        new_stacks[end-1] = crates + new_stacks[end-1]
    return ''.join([x[0] for x in new_stacks])

print('Part 1:', move_crates(stacks, data))


# Part two
print('Part 2:', move_crates(stacks, data, True))