import re

# Part one
def calc_safety_factor(robots, positions):
    x_max = 101
    y_max = 103
    sum = 1

    for _ in range(100):
        for r in robots:
            curr_pos = positions[r]
            x, y = curr_pos
            vel = robots[r]
            new_pos = ((x + vel[0]) % x_max, (y + vel[1]) % y_max)
            positions[r] = new_pos

    quadrants = [
        (0, y_max // 2, 0, x_max // 2),
        (0, y_max // 2, (x_max // 2) + 1, x_max),
        ((y_max // 2) + 1, y_max, 0, x_max // 2),
        ((y_max // 2) + 1, y_max, (x_max // 2) + 1, x_max)
    ]

    for q in quadrants:
        count = 0
        for y in range(q[0], q[1]):
            for x in range(q[2], q[3]):
                count += list(positions.values()).count((x,y))
        sum *= count

    print('Part one:', sum)


# Part two
def min_secs_for_easter_egg(robots, positions):

    def print_picture(picture):
        for i in range(len(picture)):
            print(''.join(picture[i]))

    x_max = 101
    y_max = 103
    picture = [['.' for _ in range(x_max)] for _ in range(y_max)]

    for p in positions:
        x, y = positions[p]
        picture[y][x] = '#'

    for i in range(9999):
        for r in robots:
            curr_pos = positions[r]
            x, y = curr_pos
            vel = robots[r]
            new_pos = ((x + vel[0]) % x_max, (y + vel[1]) % y_max)
            positions[r] = new_pos
            picture[y][x] = '.'
            picture[new_pos[1]][new_pos[0]] = '#'

        if len(list(positions.values())) == len(set(positions.values())):
            # print_picture(picture)
            print('Part two:', i+1)
            break


def main():
    with open('inputs/day-14.in', 'r') as file:
        data = file.read().strip().split('\n')

    robots = {}
    positions = {}

    for i in range(len(data)):
        nums = tuple(map(int, re.match(r"p=([-+]?\d+),([-+]?\d+) v=([-+]?\d+),([-+]?\d+)", data[i]).group(1,2,3,4)))
        robots[i] = (nums[2], nums[3])
        positions[i] = (nums[0], nums[1])

    calc_safety_factor(robots.copy(), positions.copy())
    min_secs_for_easter_egg(robots.copy(), positions.copy())

if __name__ == '__main__':
    main()
