# Part one
def stones_after_25_blinks(data):
    stones = [_ for _ in data]

    for _ in range(25):
        new_stones = []
        for n in stones:

            if n == 0:
                new_stones.append(1)
            elif len(str(n)) % 2 == 0:
                nstr = str(n)
                l = len(nstr)
                new_stones.append(int(nstr[:l // 2]))
                new_stones.append(int(nstr[l // 2:]))
            else:
                new_stones.append(n * 2024)

            stones = new_stones

    print('Part one:', len(stones))


# Part two
def stones_after_75_blinks(data):
    cache = {}

    def dnc(n, step):
        if step == 0:
            return 1

        if n == 0:
            if (n,step) in cache:
                return cache[(n,step)]

            res = dnc(1, step-1)
            cache[(n,step)] = res
            return res
        
        if len(str(n)) % 2 == 0:
            if (n,step) in cache:
                return cache[(n,step)]

            nstr = str(n)
            l = len(nstr) // 2

            res = dnc(int(nstr[:l]), step-1) + dnc(int(nstr[l:]), step-1)
            cache[(n,step)] = res
            return res

        if (n,step) in cache:
            return cache[(n,step)]
        
        res = dnc(n * 2024, step-1)
        cache[(n,step)] = res
        return res

    print('Part two:', sum([dnc(n, 75) for n in data]))


def main():
    with open('inputs/day-11.in', 'r') as file:
        data = [int(_) for _ in file.read().strip().split(' ')]

    stones_after_25_blinks(data)
    stones_after_75_blinks(data)

if __name__ == '__main__':
    main()
