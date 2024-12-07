import re

# Part one
def calc_2op_calibration(data):

    def recurse(sum, nums, results):
        if len(nums) == 0:
            results.append(sum)
            return
        
        recurse(sum + nums[0], nums[1:], results)
        recurse(sum * nums[0], nums[1:], results)

    sum = 0
    for i in range(len(data)):
        test_val = data[i][0]
        results = []
        recurse(data[i][1], data[i][2:], results)

        if test_val in results:
            sum += test_val

    print('Part one:', sum)


# Part two
def calc_3op_calibration(data):

    def recurse(sum, nums, results):
        if len(nums) == 0:
            results.append(sum)
            return
        
        recurse(sum + nums[0], nums[1:], results)
        recurse(sum * nums[0], nums[1:], results)
        recurse(int(str(sum) + str(nums[0])), nums[1:], results)

    sum = 0
    for i in range(len(data)):
        test_val = data[i][0]
        results = []
        recurse(data[i][1], data[i][2:], results)

        if test_val in results:
            sum += test_val

    print('Part two:', sum)


def main():
    with open('inputs/day-7.in', 'r') as file:
        data = [list(map(int, re.split(': | ', _))) for _ in file.read().strip().split('\n')]

    calc_2op_calibration(data)
    calc_3op_calibration(data)

if __name__ == '__main__':
    main()
