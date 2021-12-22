with open('inputs/day-21.txt') as file:
    data = file.read().split('\n')
    p1_pos, p2_pos = int(data[0][-1]), int(data[1][-1])


# Part one
p1_score = 0
p2_score = 0
dice = 0
dice_count = 0
while True:
    p1_pos = (((p1_pos + (dice + 1) + (dice + 2) + (dice + 3)) - 1) % 10) + 1
    p1_score += p1_pos
    dice = (((dice + 3) - 1) % 100) + 1
    dice_count += 3
    if p1_score >= 1000:
        break
    p2_pos = (((p2_pos + (dice + 1) + (dice + 2) + (dice + 3)) - 1) % 10) + 1
    p2_score += p2_pos
    dice = (((dice + 3) - 1) % 100) + 1
    dice_count += 3
    if p2_score >= 1000:
        break

if p1_score < p2_score:
    print(p1_score * dice_count)
else:
    print(p2_score * dice_count)


# Part two