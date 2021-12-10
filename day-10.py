class Stack:
    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1]

    def size(self):
        return len(self.__data)

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return f"[{str(self.__data)[1:-1]} <-"

with open('inputs/day-10.txt') as file:
    data = file.read().split('\n')

# Part one
def check_status(data):
    s = Stack()
    chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for char in data:
        if char in chunks:
            s.push(char)
        if char in chunks.values():
            if s.is_empty():
                return (None, None)
            if chunks[s.pop()] != char:
                return (True, char)
    return (False, None)

score = 0
scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
for line in data:
    status = check_status(line)
    if status[0] == True:
        score += scoring[status[1]]
print(score)

# Part two
def check_missing(data):
    s = Stack()
    chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for char in data:
        if char in chunks:
            s.push(char)
        if char in chunks.values():
            if s.is_empty() or chunks[s.pop()] != char:
                return None
    if not s.is_empty():
        missing = []
        while not s.is_empty():
            missing.append(chunks[s.pop()])
        return missing
    return None

scores = []
scoring = {')': 1, ']': 2, '}': 3, '>': 4}
for line in data:
    status = check_missing(line)
    if status != None:
        score = 0
        for x in status:
            score *= 5
            score += scoring[x]
        scores.append(score)

scores = sorted(scores)
print(scores[len(scores) // 2])
