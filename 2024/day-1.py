# Part one
def total_distance(left, right, size):
    sum = 0

    left = sorted(left)
    right = sorted(right)

    for i in range(size):
        sum += abs(left[i] - right[i])

    print('Part one:', sum)


# Part two
def total_counts(left, right, size):
    sum = 0

    for i in range(size):
        sum += (left[i] * right.count(left[i]))

    print('Part two:', sum)


def main():
    with open('inputs/day-1.in', 'r') as file:
        data = file.read().strip().split('\n')
        size = len(data)

        left = []
        right = []

        for i in range(size):
            nums = list(map(lambda y: int(y), data[i].strip().split()))
            left.append(nums[0])
            right.append(nums[1])

    total_distance(left, right, size)
    total_counts(left, right, size)


if __name__ == '__main__':
    main()