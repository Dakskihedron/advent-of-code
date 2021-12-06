with open('inputs/day-6.txt', 'r') as file:
    data = list(map(int, file.read().split(',')))

# Part one
days = input('Number of days: ')
fish = [x for x in data]
for _ in range(int(days)):
    for i in range(len(fish) - 1, -1, -1):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1
print(f"After {days} days: {len(fish)}")

# Part two (and technically part 1 but better)
days = input('Number of days: ')
fish = [data.count(x) for x in range(9)]
for _ in range(int(days)):
    new_fish = fish.pop(0)
    fish.append(new_fish)
    fish[6] += new_fish
print(sum(fish))
