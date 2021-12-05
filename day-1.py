with open('inputs/day-1.txt', 'r') as file:
    depths = file.read().split('\n')

# Part one
count = 0
for i in range(1, len(depths)):
    if int(depths[i]) > int(depths[i-1]):
        count += 1
print(count)

# Part two
count = 0
prev = sum([int(depths[0]), int(depths[1]), int(depths[2])])
for i in range(2, len(depths)-1):
    now = sum([int(depths[i-1]), int(depths[i]), int(depths[i+1])])
    if now > prev:
        count += 1
    prev = now
print(count)
