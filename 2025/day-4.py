# Part one
def find_number_of_accessible_rolls(data):
    sum = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '.':
                continue

            rolls = 0

            # Check top
            if y > 0:
                # Immediate
                if data[y-1][x] == '@':
                    rolls += 1

                # Top-left
                if x > 0 and data[y-1][x-1] == '@':
                    rolls += 1

                # Top-right
                if x < len(data[y])-1 and data[y-1][x+1] == '@':
                    rolls += 1

            # Check bottom
            if y < len(data)-1:
                # Immediate
                if data[y+1][x] == '@':
                    rolls += 1

                # Bottom-left
                if x > 0 and data[y+1][x-1] == '@':
                    rolls += 1

                # Bottom-right
                if x < len(data[y])-1 and data[y+1][x+1] == '@':
                    rolls += 1

            # Check left
            if x > 0 and data[y][x-1] == '@':
                rolls += 1

            # Check right
            if x < len(data[y])-1 and data[y][x+1] == '@':
                rolls += 1

            if rolls < 4:
                sum += 1

    print('Part one:', sum)


# Part two
def find_number_of_removeable_rolls(data):
    sum = 0
    grid = [[_ for _ in _] for _ in data]

    while True:
        removeable = []

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '.':
                    continue

                rolls = 0

                # Check top
                if y > 0:
                    # Immediate
                    if grid[y-1][x] == '@':
                        rolls += 1

                    # Top-left
                    if x > 0 and grid[y-1][x-1] == '@':
                        rolls += 1

                    # Top-right
                    if x < len(grid[y])-1 and grid[y-1][x+1] == '@':
                        rolls += 1

                # Check bottom
                if y < len(grid)-1:
                    # Immediate
                    if grid[y+1][x] == '@':
                        rolls += 1

                    # Bottom-left
                    if x > 0 and grid[y+1][x-1] == '@':
                        rolls += 1

                    # Bottom-right
                    if x < len(grid[y])-1 and grid[y+1][x+1] == '@':
                        rolls += 1

                # Check left
                if x > 0 and grid[y][x-1] == '@':
                    rolls += 1

                # Check right
                if x < len(grid[y])-1 and grid[y][x+1] == '@':
                    rolls += 1

                if rolls < 4:
                    removeable.append((y,x))

        if len(removeable) == 0:
            break

        sum += len(removeable)

        for i in range(len(removeable)):
            y, x = removeable[i]
            grid[y][x] = '.'

    print('Part two:', sum)


def main():
    with open('inputs/day-4.in', 'r') as file:
        data = file.read().strip().split('\n')
        data = [[_ for _ in _] for _ in data]

    find_number_of_accessible_rolls(data)
    find_number_of_removeable_rolls(data)


if __name__ == '__main__':
    main()
