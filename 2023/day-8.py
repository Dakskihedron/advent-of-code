import math


# Part one
def get_steps(data):
    instr = data[0]
    network = {n.split('=')[0].strip(): tuple(map(str, n.split('=')[1].strip()[1:-1].split(', '))) for n in data[1:]}

    steps = 0
    cnode = 'AAA'
    cinstr = 0
    while cnode != 'ZZZ':
        if instr[cinstr] == 'L':
            cnode = network[cnode][0]
        else:
            cnode = network[cnode][1]
        steps += 1
        cinstr = (cinstr + 1) % len(instr)

    print('Part one:', steps)


# Part two
def get_path_len(instr, network, start):
    steps = 0
    cnode = start
    cinstr = 0
    while cnode[2] != 'Z':
        if instr[cinstr] == 'L':
            cnode = network[cnode][0]
        else:
            cnode = network[cnode][1]
        steps += 1
        cinstr = (cinstr + 1) % len(instr)
    return steps


def get_lcm(data):
    instr = data[0]
    nodes = []
    network = {}
    for n in data[1:]:
        a,b = n.split('=')
        network[a.strip()] = tuple(map(str, b.strip()[1:-1].split(', ')))
        if a[2] == 'A':
            nodes.append(a.strip())

    path_lens = [get_path_len(instr, network, n) for n in nodes]
    print('Part two:', math.lcm(*path_lens))


def main():
    with open('inputs/day-8.in', 'r') as file:
        data = [_ for _ in file.read().strip().split('\n') if _ != '']
    get_steps(data)
    get_lcm(data)


if __name__ == '__main__':
    main()