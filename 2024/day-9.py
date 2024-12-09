# Part one
def calc_single_block_checksum(data):
    fs = []
    id = 0

    for i in range(len(data)):
        if i % 2 == 0:
            fs += [id] * data[i]
            id += 1
        else:
            fs += ['.'] * data[i]

    m, n = 0, len(fs)-1
    while True:
        if (m > len(fs)-1) or (n < 0) or (m >= n):
            break

        if fs[m] == '.' and fs[n] != '.':
            fs[m], fs[n] = fs[n], fs[m]

        if fs[m] != '.':
            m += 1

        if fs[n] == '.':
            n -= 1

    fs = fs[:fs.index('.')]
    checksum = sum([fs[i] * i for i in range(len(fs))])
    print('Part one:', checksum)


# Part two
def calc_whole_block_checksum(data):
    fs = {}
    files = {}
    spaces = {}
    id = 0

    index = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(index, index+data[i]):
                fs[j] = id
            files[id] = [_ for _ in range(index, index+data[i])]
            id += 1
        else:
            for j in range(index, index+data[i]):
                fs[j] = '.'
            spaces[id-1] = [_ for _ in range(index, index+data[i])]
        index += data[i]

    f = len(files.keys()) - 1
    while True:
        if f < 0:
            break

        for s in range(len(spaces.keys())):
            if len(spaces[s]) >= len(files[f]) and (s <= f):
                for i in spaces[s][:len(files[f])]:
                    fs[i] = f
                for i in files[f]:
                    fs[i] = '.'
                spaces[s] = spaces[s][len(files[f]):]
                break
        
        f -= 1

    checksum = sum([fs[_] * _ if fs[_] != '.' else 0 for _ in range(len(fs))])
    print('Part two:', checksum)


def main():
    with open('inputs/day-9.in', 'r') as file:
        data = list(map(int, [_ for _ in file.read().strip()]))

    calc_single_block_checksum(data)
    calc_whole_block_checksum(data)

if __name__ == '__main__':
    main()
