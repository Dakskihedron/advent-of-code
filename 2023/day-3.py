from collections import defaultdict
from functools import reduce


# Part one and two
def calc_gear_ratios(data):
    part_num_sum = 0
    gear_pairs = defaultdict(list)
    max_y = len(data)-1
    max_x = len(data[0])-1

    for y in range(len(data)):
        x = 0
        num = ''
        is_part = False

        gears = []

        while x < max_x+1:
            # Add digits to num string, else continue.
            if data[y][x].isdigit():
                num += data[y][x]
            else:
                x += 1
                continue

            # Check neighbours if not already part number.
            if not is_part:
                # Check neighbours on left.
                if x > 0:
                    # Left
                    if data[y][x-1] != '.' and not data[y][x-1].isdigit():
                        is_part = True
                        if data[y][x-1] == '*':
                            gears.append((y,x-1))
                    # Top-left
                    elif y > 0 and data[y-1][x-1] != '.' and not data[y-1][x-1].isdigit():
                        is_part = True
                        if data[y-1][x-1] == '*':
                            gears.append((y-1,x-1))
                    # Bottom-left
                    elif y < max_y and data[y+1][x-1] != '.' and not data[y+1][x-1].isdigit():
                        is_part = True
                        if data[y+1][x-1] == '*':
                            gears.append((y+1,x-1))

                # Check neighbours on right.
                if x < max_x:
                    # Right
                    if data[y][x+1] != '.' and not data[y][x+1].isdigit():
                        is_part = True
                        if data[y][x+1] == '*':
                            gears.append((y,x+1))
                    # Top-right
                    elif y > 0 and data[y-1][x+1] != '.' and not data[y-1][x+1].isdigit():
                        is_part = True
                        if data[y-1][x+1] == '*':
                            gears.append((y-1,x+1))
                    # Bottom-right
                    elif y < max_y and data[y+1][x+1] != '.' and not data[y+1][x+1].isdigit():
                        is_part = True
                        if data[y+1][x+1] == '*':
                            gears.append((y+1,x+1))

                # Top
                if y > 0:
                    if data[y-1][x] != '.' and not data[y-1][x].isdigit():
                        is_part = True
                        if data[y-1][x] == '*':
                            gears.append((y-1,x))
                
                # Bottom
                if y < max_y:
                    if data[y+1][x] != '.' and not data[y+1][x].isdigit():
                        is_part = True
                        if data[y+1][x] == '*':
                            gears.append((y+1,x))

            x += 1
            if x == max_x+1 or not data[y][x].isdigit():
                if is_part:
                    part_num_sum += int(num)
                    for g in gears:
                        gear_pairs[g] += [int(num)]
                    gears = []
                num = ''
                is_part = False

    gear_ratios_sum = 0
    for key in gear_pairs:
        if len(gear_pairs[key]) == 2:
            gear_ratios_sum += reduce((lambda a,b: a*b), gear_pairs[key])

    print('Part one:', part_num_sum)
    print('Part two:', gear_ratios_sum)



def main():
    with open('inputs/day-3.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [[_ for _ in line] for line in data]
    calc_gear_ratios(data)


if __name__ == '__main__':
    main()