# Part one
def add(elf):
    elf = [int(x) for x in elf.strip().split('\n')]
    return sum(elf)

with open('inputs/day-1.txt', 'r') as file:
    elves = list(map(add, file.read().strip().split('\n\n')))
    print('Part 1:', max(elves))


# Part two
elves.sort()
print('Part 2:', sum(elves[-3:]))