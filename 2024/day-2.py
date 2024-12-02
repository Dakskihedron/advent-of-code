# Part one
def total_safe_reports(data):
    sum = 0
    for i in range(len(data)):
        nums = data[i]
        diffs = [y-x for x, y in zip(nums[:-1], nums[1:])]
        if all(1 <= n <= 3 for n in diffs) or all(-1 >= n >= -3 for n in diffs):
            sum += 1

    print('Part one:', sum)


# Part two
def total_safe_reports_after_dampening(data):

    def check_safe(diffs):
        if all(1 <= n <= 3 for n in diffs) or all(-1 >= n >= -3 for n in diffs):
            return True
        return False

    sum = 0
    for i in range(len(data)):
        nums = data[i]
        diffs = [y-x for x, y in zip(nums[:-1], nums[1:])]

        if check_safe(diffs):
            sum += 1
        else:
            for j in range(len(nums)):
                new_nums = nums[:j] + nums[j+1:]
                diffs = [y-x for x, y in zip(new_nums[:-1], new_nums[1:])]
                if check_safe(diffs):
                    sum += 1
                    break

    print('Part two:', sum)


def main():
    with open('inputs/day-2.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = list(map(lambda _: list(map(lambda _: int(_), _.strip().split())), data))

    total_safe_reports(data)
    total_safe_reports_after_dampening(data)


if __name__ == '__main__':
    main()