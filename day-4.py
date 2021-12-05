numbers = [93,18,74,26,98,52,94,23,15,2,34,75,13,31,39,76,96,16,84,12,38,27,8,85,86,43,4,79,57,19,40,59,14,21,35,0,90,11,32,17,78,83,54,42,66,82,99,45,55,63,24,5,89,46,80,49,3,48,67,47,50,60,81,51,71,33,72,6,9,30,56,20,77,29,28,69,25,36,91,92,65,22,62,58,64,88,10,7,87,41,44,37,73,70,68,97,61,95,53,1]

with open('inputs/day-4.txt', 'r') as file:
    content = file.read().split('\n\n')
    for i in range(0, len(content)):
        content[i] = content[i].split('\n')
        for j in range(0, len(content[i])):
            content[i][j] = [int(x) for x in content[i][j].split()]

def check_bingo(board):
    for row in range(len(board)):
        if board[row].count('x') == len(board[row]):
            return True
        for number in range(len(board[row])):
            column = [row[number] for row in board]
            if column.count('x') == len(column):
                return True

# # Part one
boards = [[[x for x in y] for y in z] for z in content]
board = None
value = None

for bingo in numbers:
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for n in range(len(boards[b][r])):
                if boards[b][r][n] == bingo:
                    boards[b][r][n] = 'x'

                    if check_bingo(boards[b]):
                        board = boards[b]
                        value = bingo
                        break
            if board:
                break
        if board:
            break
    if board:
        break

for row in board:
    print(row)
print(value)

unmarked = sum([n for r in board for n in r if n != 'x'])
print(unmarked * value)

# Part two
boards = [[[x for x in y] for y in z] for z in content]
board = None
value = None

for bingo in numbers:
    for b in range(len(boards)):
        if boards[b] == None:
            continue
        for r in range(len(boards[b])):
            for n in range(len(boards[b][r])):
                if boards[b][r][n] == bingo:
                    boards[b][r][n] = 'x'

                    if boards.count(None) == len(boards) - 1:
                        board = boards
                        value = bingo
                        break

                    if check_bingo(boards[b]):
                        boards[b] = None
                        break
                if boards[b] == None:
                    break
            if boards[b] == None:
                break
    if board:
        break

for b in board:
    if b != None:
        for row in b:
            print(row)
        print(value)
        board = b

unmarked = sum([n for r in board for n in r if n != 'x'])
print(unmarked * value)