# Part one
def add(elf):
    elf = [int(x) for x in elf.strip().split('\n')]
    return sum(elf)

with open('inputs/day-1.txt', 'r') as file:
    elves = list(map(add, file.read().split('\n\n')))
    print(max(elves))

# Part two
elves.sort()
print(sum(elves[-3:]))