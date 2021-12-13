with open('inputs/day-13.txt') as file:
    points, folds = file.read().split('\n\n')
    points = [tuple(map(int, x.split(','))) for x in points.split('\n')]
    folds = [(axis[-1], int(val)) for x in folds.split('\n') for axis, val in [x.split('=')]]

# Part one
x_max = max(x for x, _ in points)
y_max = max(y for _, y in points)
grid = [[False for _ in range(x_max+1)] for _ in range(y_max+1)]

for x, y in points:
    grid[y][x] = True

def fold_x(grid, fold_point):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] and x > fold_point:
                grid[y][2 * fold_point - x] = grid[y][x] or grid[y][2 * fold_point - x]
        grid[y] = grid[y][:fold_point]
    return grid

def fold_y(grid, fold_point):
    for y in range(len(grid)):
        if y > fold_point:
            for x in range(len(grid[y])):
                if grid[y][x]:
                    grid[2 * fold_point - y][x] = grid[y][x] or grid[2 * fold_point - y][x]
    return grid[:fold_point]

def fold(grid, fold_axis, fold_point):
    if fold_axis == 'x':
        return fold_x(grid, fold_point)
    return fold_y(grid, fold_point)

print(f"After one fold, we have {sum([1 for row in fold(grid, 'x', 655) for x in row if x])} dots.")
    
# Part two
for fold_axis, fold_point in folds:
    grid = fold(grid, fold_axis, fold_point)
print('\n'.join([' '.join(['#' if c else ' ' for c in row]) for row in grid]))