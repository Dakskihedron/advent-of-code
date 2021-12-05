with open('inputs/day-1.txt', 'r') as file:
    data = file.read().split('\n')

# Part one
count = 0
for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):
        count += 1
print(count)

# Part two
count = 0
prev = sum([int(data[0]), int(data[1]), int(data[2])])
for i in range(2, len(data)-1):
    now = sum([int(data[i-1]), int(data[i]), int(data[i+1])])
    if now > prev:
        count += 1
    prev = now
print(count)
