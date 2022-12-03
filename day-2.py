with open('inputs/day-2.txt', 'r') as file:
    data = file.read().split('\n')
    rounds = [x.strip().split(' ') for x in data]

# Part 1
scoring = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}
score = 0
for r in rounds:
    if scoring[r[0]] == scoring[r[1]]:
        score += (3 + scoring[r[1]])
    elif (r[0] == 'A' and r[1] == 'Z'):
        score += scoring[r[1]]
    elif (r[0] == 'C' and r[1] == 'X') or (scoring[r[0]] < scoring[r[1]]):
        score += (6 + scoring[r[1]])
    else:
        score += scoring[r[1]]
print(score)

# Part two
score = 0
for r in rounds:
    if r[1] == 'X':
        score += ((scoring[r[0]] - 2) % 3) + 1
    elif r[1] == 'Y':
        score += (3 + scoring[r[0]])
    else:
        score += (6 + (scoring[r[0]] % 3) + 1)
print(score)
