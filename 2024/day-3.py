import re

# Part one
def total_mul(data):
    sum = 0

    for i in range(len(data)):
        substrs = re.findall('(mul\\(\\d+,\\d+\\))', data[i])

        for j in range(len(substrs)):
            nums = re.findall('(\\d+)', substrs[j])
            x, y = nums
            sum += int(x) * int(y)

    print('Part one:', sum)


# Part two
def total_enabled_mul(data):
    sum = 0
    enabled = True

    for i in range(len(data)):
        substrs = re.findall('(don\'t\\(\\)|do\\(\\)|mul\\(\\d+,\\d+\\))', data[i])

        for j in range(len(substrs)):
            val = substrs[j]
            if val == 'don\'t()':
                enabled = False
            elif val == 'do()':
                enabled = True
            else:
                if enabled:
                    nums = re.findall('(\\d+)', val)
                    x, y = nums
                    sum += int(x) * int(y)

    print('Part two:', sum)


def main():
    with open('inputs/day-3.in', 'r') as file:
        data = file.read().strip().split('\n')

    total_mul(data)
    total_enabled_mul(data)

if __name__ == '__main__':
    main()