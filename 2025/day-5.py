# Part one
def find_number_of_fresh_ingredients(ranges, ids):
    sum = 0

    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                sum += 1
                break

    print('Part one:', sum)


# Part two
def find_number_of_fresh_ingredient_ids(ranges):
    sum = 0

    r_sorted = sorted(ranges, key=lambda _: _[0])
    r_merged = []

    for r in r_sorted:
        if len(r_merged) > 0 and r[0] <= r_merged[-1][1]:
            r_merged[-1][1] = max(r[1], r_merged[-1][1])
        else:
            r_merged.append(r)

    for r in r_merged:
        sum += (r[1] + 1) - r[0]

    print('Part two:', sum)


def main():
    with open('inputs/day-5.in', 'r') as file:
        data = file.read().strip().split('\n')
        ranges, ids = [[int(_.split('-')[0]), int(_.split('-')[1])] for _ in data[:data.index('')]], [int(_) for _ in data[data.index('')+1:]]

    find_number_of_fresh_ingredients(ranges, ids)
    find_number_of_fresh_ingredient_ids(ranges)


if __name__ == '__main__':
    main()
