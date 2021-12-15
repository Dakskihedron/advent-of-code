with open('inputs/day-14.txt') as file:
    template, pairs = file.read().split('\n\n')
    pairs = [pair.split(' -> ') for pair in pairs.split('\n')]
    rules = {x: y for x, y in pairs}


# Part one
steps = 10
polymer = template
while steps != 0:
    elements = [(rules[polymer[i] + polymer[i+1]], i+1) for i in range(len(polymer) - 1)]
    new_polymer = [x for x in polymer]
    for x, y in elements[::-1]:
        new_polymer.insert(y, x)
    polymer = ''.join(new_polymer)
    steps -= 1

elements_count = [polymer.count(x) for x in set([x for x in rules.values()])]
print(max(elements_count) - min(elements_count))


# Part two (and technically improved part one)
steps = 40

elements_count = {i: 0 for i in set(rules.values())}
for i in template:
    elements_count[i] += 1

rules_count = {i: 0 for i in rules.keys()}
for i in range(len(template) - 1):
    rules_count[template[i] + template[i+1]] += 1

while steps != 0:
    new_dict = {i: 0 for i in rules.keys()}
    for rule, count in rules_count.items():
        if count > 0:
            x = rules[rule]
            new_dict[rule[0] + x] += count
            new_dict[x + rule[1]] += count
            elements_count[x] += count
    rules_count = new_dict
    steps -= 1

counts = [x for x in elements_count.values()]
print(max(counts) - min(counts))