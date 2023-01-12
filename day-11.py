import math

with open('inputs/day-11.txt', 'r') as file:
    data = file.read().strip().split('\n\n')
    data = [x.split('\n') for x in data]


# Part one
def calculate_monkey_biz(rounds, reduce_worry, data):
    inspected = {}
    holding = {}
    div_checks = {}

    for m in range(len(data)):
        inspected[m] = 0
        holding[m] = [int(x) for x in data[m][1].strip().split(':')[1].split(',')]
        div_checks[m] = int(data[m][3].strip().split(' ')[3])

    prod = math.lcm(*list(div_checks.values()))

    for _ in range(rounds):
        for m in range(len(data)):
            for n in range(len(holding[m])):
                old = holding[m][n]
                op = data[m][2].strip().split(':')[1][7:]
                new = eval(op)

                if not reduce_worry:
                    new = int(new // 3)
                else:
                    new %= prod

                div = int(data[m][3].strip().split(' ')[3])
                if new % div == 0:
                    j = int(data[m][4].strip().split(' ')[5])
                else:
                    j = int(data[m][5].strip().split(' ')[5])
                holding[j] += [new]
                inspected[m] += 1
            holding[m] = []

    sorted_inspected = sorted(list(inspected.values()))
    return (sorted_inspected[-1] * sorted_inspected[-2])

print('Part 1:', calculate_monkey_biz(20, False, data))


# Part two
print('Part 2:', calculate_monkey_biz(10000, True, data))