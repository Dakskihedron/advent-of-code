with open('inputs/day-17.txt') as file:
    data = file.read().replace(', y', '').split('=')
    xbounds, ybounds = tuple(map(int, data[1].split('..'))), tuple(map(int, data[2].split('..')))


# Part one (holy shit, thanks u/Tetrat)
y = abs(ybounds[0])
print(y * (y - 1) // 2)


# Part two
def fire_probe(vel):
    x, y = 0, 0
    xvel, yvel = vel
    while (x < xbounds[1] + 1 and not (xvel == 0 and x < xbounds[0])) and not (x > xbounds[0] and y < ybounds[0]):
        x += xvel
        y += yvel
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1
        if (x in range(xbounds[0], xbounds[1] + 1)) and (y in range(ybounds[0], ybounds[1] + 1)):
            return True
    return False

count = 0
for x in range(-500, 500):
    for y in range(-500, 500):
        result = fire_probe((x, y))
        if result:
            count += 1
print(count)