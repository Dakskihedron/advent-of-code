with open('inputs/day-7.txt', 'r') as file:
    data = file.read().strip().split('\n')


# Part one
dir_dict = {}
dir_list = []
for line in data:
    output = line.split(' ')
    if output[1] == 'cd':
        if output[2] == '/':
            dir_list = ['/']
        elif output[2] == '..':
            dir_list.pop()
        else:
            dir_list.append(output[2])
    elif output[0].isnumeric():
        for n in range(0, len(dir_list)):
            path = '/'.join(dir_list[:n+1])
            if path in dir_dict:
                dir_dict[path] += int(output[0])
            else:
                dir_dict[path] = int(output[0])

print('Part 1:', sum([x for x in dir_dict.values() if x <= 100000]))


# Part two
curr_unused = 70000000 - dir_dict['/']
print('Part 2:', min([x for x in dir_dict.values() if (curr_unused + x) >= 30000000]))