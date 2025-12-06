from functools import reduce


# Part one
def total_of_individual_problems(data):
    total = 0

    data = [_.strip().split() for _ in data]
    height = len(data)

    for i in range(len(data[0])):
        ops = [int(data[j][i]) for j in range(height-1)]
        operator = data[height-1][i]

        if operator == '*':
            total += reduce(lambda m, n: m*n, ops)
        else:
            total += sum(ops)

    print('Part one:', total)


# Part two
def total_of_individual_problems_corrected(data):
    total = 0

    groupings = {}
    group_n = 0
    group_l = 1

    for i in range(len(data[-1])):
        if i == len(data[-1])-1:
            groupings[group_n] = group_l + 1
            break

        val = data[-1][i]
        if val == '*' or val == '+':
            if group_l > 1:
                groupings[group_n] = group_l - 1
                group_n = i
                group_l = 1
        else:
            group_l += 1

    height = len(data)
    ops = []
    ops_i = 0
    ops_l = 0

    for i in range(len(data[-1])):
        if i in groupings.keys():
            ops_i = i
            ops_l = groupings[i]
            ops = []
        else:
            ops_l -= 1

        if ops_l > 0:
            num = ''
            for j in range(height-1):
                num += data[j][i]

            ops.append(int(num))

        if i != 0 and (ops_l == 0 or i == len(data[0])-1):
            operator = data[-1][ops_i]
            if operator == '*':
                total += reduce(lambda m, n: m*n, ops)
            else:
                total += sum(ops)

    print('Part two:', total)


def main():
    with open('inputs/day-6.in', 'r') as file:
        data = file.read().split('\n')
        if '' in data:
            data.remove('')

    total_of_individual_problems(data)
    total_of_individual_problems_corrected(data)


if __name__ == '__main__':
    main()
