import re
from fractions import Fraction

# Part one
def fewest_tokens(data):
    sum = 0

    for p in data:
        a = p['A'][0]
        b = p['B'][0]
        c = p['A'][1]
        d = p['B'][1]
        px = p['prize'][0]
        py = p['prize'][1]

        determinant = (a * d) - (b * c)

        x = Fraction(((d * px) + (-b * py)), determinant)
        y = Fraction(((-c * px) + (a * py)), determinant)

        if x.is_integer() and y.is_integer():
            sum += (3 * x) + y

    print('Part one:', sum)


# Part two
def fewest_tokens_10000000000000(data):
    sum = 0

    for p in data:
        a = p['A'][0]
        b = p['B'][0]
        c = p['A'][1]
        d = p['B'][1]
        px = p['prize'][0] + 10000000000000
        py = p['prize'][1] + 10000000000000

        determinant = (a * d) - (b * c)

        x = Fraction(((d * px) + (-b * py)), determinant)
        y = Fraction(((-c * px) + (a * py)), determinant)

        if x.is_integer() and y.is_integer():
            sum += (3 * x) + y

    print('Part two:', sum)


def main():
    with open('inputs/day-13.in', 'r') as file:
        data = [[_ for _ in _.split('\n')] for _ in file.read().strip().split('\n\n')]

    processed_data = []
    for i in range(len(data)):
        machine = data[i]
        config = {}
        config['A'] = tuple([int(_) for _ in re.match(r"Button A: X\+([-+]?\d+), Y\+([-+]?\d+)", machine[0]).group(1, 2)])
        config['B'] = tuple([int(_) for _ in re.match(r"Button B: X\+([-+]?\d+), Y\+([-+]?\d+)", machine[1]).group(1, 2)])
        config['prize'] = tuple([int(_) for _ in re.match(r"Prize: X=([-+]?\d+), Y=([-+]?\d+)", machine[2]).group(1, 2)])
        processed_data.append(config)

    fewest_tokens(processed_data)
    fewest_tokens_10000000000000(processed_data)

if __name__ == '__main__':
    main()
