with open('inputs/day-2.txt') as file:
    instructions = file.read().split('\n')
    for i in range(len(instructions)):
        instructions[i] = instructions[i].split()

# Part one
h_pos = 0
depth = 0
for step in instructions:
    if step[0] == 'forward':
        h_pos += int(step[1])
    elif step[0] == 'down':
        depth += int(step[1])
    else:
        depth -= int(step[1])
print(h_pos * depth)

# Part two
h_pos = 0
depth = 0
aim = 0
for step in instructions:
    if step[0] == 'forward':
        h_pos += int(step[1])
        depth += aim * int(step[1])
    elif step[0] == 'down':
        aim += int(step[1])
    else:
        aim -= int(step[1])
print(h_pos * depth)