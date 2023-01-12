with open('inputs/day-7.txt') as file:
    data = list(map(int, file.read().split(',')))

# Part one
usage_list = []
for i in range(len(data)):
    fuel_usage = 0
    for number in [x for x in data if x != data[i]]:
        fuel_usage += abs(number - data[i])
    usage_list.append(fuel_usage)
print(min(usage_list))

# Part two
usage_list = []
for i in range(len(data)):
    fuel_usage = 0
    for number in [x for x in data if x != i]:
        calc_fuel = lambda x: int((x ** 2 + x) / 2)
        fuel_usage += calc_fuel(abs(number - i))
    usage_list.append(fuel_usage)
print(min(usage_list))