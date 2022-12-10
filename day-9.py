with open('inputs/day-9.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = [x.split(' ') for x in data]

# Part one
def count_traversed(knots_coords, data):
    tail_coords = set()

    for move in data:
        step, steps = -1 if move[0] in 'LU' else 1, int(move[1])

        for _ in range(steps):
            for n in range(len(knots_coords)):
                tail = knots_coords[n]

                if n == 0:
                    if move[0] in 'LR':
                        tail[0] += step
                    else:
                        tail[1] += step
                
                else:
                    head = knots_coords[n-1]

                    # Check if head is adjacent
                    if (abs(tail[0] - head[0]) == 1 and abs(tail[1] - head[1]) == 1) \
                        or (tail == head) \
                        or (tail[0] == head[0] and abs(tail[1] - head[1]) == 1) \
                        or (tail[1] == head[1] and abs(tail[0] - head[0]) == 1):

                        if n == len(knots_coords) - 1:
                            tail_coords.add(tuple(tail))
                    
                    else:
                        if head[0] > tail[0] or head[0] < tail[0]:
                            tail[0] += 1 if head[0] > tail[0] else -1
                    
                        if head[1] > tail[1] or head[1] < tail[1]:
                            tail[1] += 1 if head[1] > tail[1] else -1

                        if n == len(knots_coords) - 1:
                            tail_coords.add(tuple(tail))

    return len(tail_coords)

print(count_traversed([[0,0], [0,0]], data))


# Part 2
print(count_traversed([[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]], data))