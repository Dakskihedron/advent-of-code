import re


# Part one
def sum_calibration1(data):
    sum = 0
    numbers = r"(\W*(1|2|3|4|5|6|7|8|9)\W*)"
    for line in data:
        sum += int(re.search(numbers, line).group(1) + re.search(numbers, line[::-1]).group(1))
    print('Part one:', sum)


# Part two
def sum_calibration2(data):
    sum = 0
    words = r"(\W*(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)\W*)"
    words_back = r"(\W*(1|2|3|4|5|6|7|8|9|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)\W*)"

    word_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in data:
        num = ''

        a = re.search(words, line).group(1)
        b = re.search(words_back, line[::-1]).group(1)

        if a.isdigit():
            num += a
        else:
            num += word_to_digit[a]
        if b.isdigit():
            num += b
        else:
            num += word_to_digit[b[::-1]]
        sum += int(num)

    print('Part two:', sum)


def main():
    with open('inputs/day-1.in', 'r') as file:
        data = file.read().strip().split('\n')

    sum_calibration1(data)
    sum_calibration2(data)


if __name__ == '__main__':
    main()