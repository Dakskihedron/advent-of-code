with open('inputs/day-8.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [[int(y) for y in x] for x in data]


# Part one
def check_less(val, val_list):
    for n in val_list:
        if val <= n:
            return False
    return True

count = 0
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if x == 0 or y == 0 or x == len(data[y]) - 1 or y == len(data) - 1:
            count += 1
            continue

        if x > 0:
            trees_left = [data[y][n] for n in range(0, x)]

        if x < len(data[y]) - 1:
            trees_right = [data[y][n] for n in range(x+1, len(data[x]))]

        if y > 0:
            trees_up = [data[n][x] for n in range(0, y)]

        if y < len(data) - 1:
            trees_down = [data[n][x] for n in range(y+1, len(data))]

        for trees in [trees_left, trees_right, trees_up, trees_down]:
            if check_less(data[y][x], trees):
                count += 1
                break

print('Part 1:', count)


# Part two
def get_vis(val, val_list):
    vis_list = []
    for n in val_list:
        vis_list.append(n)
        if n >= val:
            break
    return len(vis_list)

score = 0
for y in range(0, len(data)):
    for x in range(0, len(data[y])):

        trees_left = get_vis(data[y][x], [data[y][n] for n in range(0, x)][::-1]) if x > 0 else 1
        trees_right = get_vis(data[y][x], [data[y][n] for n in range(x+1, len(data[x]))]) if x < len(data[y]) - 1 else 1
        trees_up = get_vis(data[y][x], [data[n][x] for n in range(0, y)][::-1]) if y > 0 else 1
        trees_down = get_vis(data[y][x], [data[n][x] for n in range(y+1, len(data))]) if y < len(data) - 1 else 1

        scenic_score = trees_left * trees_right * trees_up * trees_down
        if scenic_score > score:
            score = scenic_score

print('Part 2:', score)
