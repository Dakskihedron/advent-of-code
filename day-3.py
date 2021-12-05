with open('inputs/day-3.txt') as file:
    report = file.read().split('\n')

# Part one
gamma = ''
epsilon = ''
for bit in range(12):
    zeroes = 0
    ones = 0

    for number in report:
        if number[bit] == '0':
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))

# Part two
oxygen = [i for i in report]
co2 = [i for i in report]

for bit in range(12):
    zeroes = 0
    ones = 0

    for n in oxygen:
        if n[bit] == '0':
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        for i in range(len(oxygen) - 1, -1, -1):
            if len(oxygen) == 1:
                break
            if oxygen[i][bit] == '1':
                oxygen.pop(i)
    else:
        for i in range(len(oxygen) - 1, -1, -1):
            if len(oxygen) == 1:
                break
            if oxygen[i][bit] == '0':
                oxygen.pop(i)

    if len(oxygen) == 1:
        break

for bit in range(12):
    zeroes = 0
    ones = 0

    for n in co2:
        if n[bit] == '0':
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        for i in range(len(co2) - 1, -1, -1):
            if len(co2) == 1:
                break
            if co2[i][bit] == '0':
                co2.pop(i)
    else:
        for i in range(len(co2) - 1, -1, -1):
            if len(co2) == 1:
                break
            if co2[i][bit] == '1':
                co2.pop(i)

    if len(co2) == 1:
        break

print(oxygen, co2)

print(int(oxygen[0], 2) * int(co2[0], 2))
