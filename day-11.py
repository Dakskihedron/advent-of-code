class Queue:
    def __init__(self):
        self.__data = []

    def enqueue(self, value):
        self.__data.insert(0, value)

    def dequeue(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1]

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return f"-> |{str(self.__data)[1:-1]}| ->"

with open('inputs/day-11.txt') as file:
    data = file.read().split('\n')
    data = [list(map(int, x)) for x in data]

# Part one
def get_adjacent(coord, data):
    adjacent = []
    if coord[0] > 0:
        adjacent.append((coord[0] - 1, coord[1]))
        if coord[1] > 0:
            adjacent.append((coord[0] - 1, coord[1] - 1))
        if coord[1] < len(data[coord[0]]) - 1:
            adjacent.append((coord[0] - 1, coord[1] + 1))
    if coord[0] < len(data) - 1:
        adjacent.append((coord[0] + 1, coord[1]))
        if coord[1] > 0:
            adjacent.append((coord[0] + 1, coord[1] - 1))
        if coord[1] < len(data[coord[0]]) - 1:
            adjacent.append((coord[0] + 1, coord[1] + 1))
    if coord[1] > 0:
        adjacent.append((coord[0], coord[1] - 1))
    if coord[1] < len(data[coord[0]]) - 1:
        adjacent.append((coord[0], coord[1] + 1))
    return adjacent

flashes = 0
steps = int(input("Number of steps: "))
curr_step = 0
energy_data = list(list(i) for i in data)
matrix_size = len(energy_data) * len(energy_data[0])

while steps != 0:
    q = Queue()

    for y in range(len(energy_data)):
        for x in range(len(energy_data[y])):
            energy_data[y][x] += 1
            if energy_data[y][x] > 9:
                energy_data[y][x] = 'f'
                flashes += 1
                q.enqueue((y, x))

    while not q.is_empty():
        coord = q.dequeue()
        for i in get_adjacent(coord, energy_data):
            if energy_data[i[0]][i[1]] != 'f':
                energy_data[i[0]][i[1]] += 1
                if energy_data[i[0]][i[1]] > 9:
                    energy_data[i[0]][i[1]] = 'f'
                    flashes += 1
                    q.enqueue((i[0], i[1]))

    for y in range(len(energy_data)):
        for x in range(len(energy_data[y])):
            if energy_data[y][x] == 'f':
                energy_data[y][x] = 0

    steps -= 1
    curr_step += 1

    # Part two
    flash_count = 0
    for row in energy_data:
        flash_count += row.count(0)
    if flash_count == matrix_size:
        print(f"Simultaneous flash after step {curr_step}.")

print(f"There are {flashes} flashes.")
