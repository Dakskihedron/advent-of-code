with open('inputs/day-10.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [x.split(' ') for x in data]

# Part one
signal_sum, cycle, x = 0, 0, 1
cycles = [20, 60, 100, 140, 180, 220]
for i in data:
    if i[0] == 'noop':
        cycle += 1
        if cycle in cycles:
            signal_sum += cycle * x
        continue
    else:
        for _ in range(2):
            cycle += 1
            if cycle in cycles:
                signal_sum += cycle * x
        x += int(i[1])

print(signal_sum)


# Part two
def check_cycle(cycle, pixel, row):
    if cycle % 40 == 0:
        pixel = 0
        row += 1
    else:
        pixel += 1
    return pixel, row

crt = [['' for _ in range(40)] for _ in range(6)]
cycle, x, row, pixel = 0, 1, 0, 0

for i in data:
    sprite = [x-1, x, x+1]

    if i[0] == 'noop':
        crt[row][pixel] = '\u2588' if pixel in sprite else '.'
        cycle += 1
        pixel, row = check_cycle(cycle, pixel, row)
    else:
        for _ in range(2):
            crt[row][pixel] = '\u2588' if pixel in sprite else '.'
            cycle += 1
            pixel, row = check_cycle(cycle, pixel, row)

        x += int(i[1])

for row in crt:
    print(''.join(row))