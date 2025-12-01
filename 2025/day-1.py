# Part one
def total_times_dial_at_zero(data):
    count = 0
    dial = 50

    for i in range(0, len(data)):
        dial = (dial + data[i]) % 100
        if dial == 0:
            count += 1

    print('Part one:', count)


# Part two
def total_times_dial_clicks_zero(data):
    count = 0
    dial = 50

    for i in range(0, len(data)):
        x = data[i]
        for _ in range(abs(x)):
            if x < 0:
                dial = (dial - 1) % 100
            else:
                dial = (dial + 1) % 100

            if dial == 0:
                count += 1

    print('Part two:', count)


def main():
    with open('inputs/day-1.in', 'r') as file:
        data = file.read().strip().split('\n');
        data = [-int(_[1:]) if _[0] == 'L' else int(_[1:]) for _ in data]

    total_times_dial_at_zero(data)
    total_times_dial_clicks_zero(data)


if __name__ == '__main__':
    main()