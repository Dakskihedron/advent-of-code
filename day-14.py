with open('inputs/day-14.txt') as file:
    template, pairs = file.read().split('\n\n')
    pairs = pairs.split('\n')
    rules = {}
    for pair in pairs:
        rule, element = pair.strip().split(' -> ')
        rules[rule] = element

# Part one
polymer = template
steps = 10
while steps != 0:
    elements = []
    for i in range(len(polymer) - 1):
        elements.append((rules[polymer[i] + polymer[i+1]], i+1))
    new_polymer = [x for x in polymer]
    for e, i in elements[::-1]:
        new_polymer.insert(i, e)
    polymer = ''.join(new_polymer)
    steps -= 1

e_list = []
for e in rules.values():
    if e not in e_list:
        e_list.append(e)
e_count = [polymer.count(e) for e in e_list]
print(max(e_count) - min(e_count))

# Part two (and technically improved part one)
steps = 40

elements_count = {}
for e in rules.values():
    if e not in elements_count:
        elements_count[e] = 0
for i in template:
    elements_count[i] += 1

rules_count = {i: 0 for i in rules.keys()}
for i in range(len(template) - 1):
    rules_count[template[i] + template[i+1]] += 1

while steps != 0:
    new_dict = {i: 0 for i in rules.keys()}
    for rule, count in rules_count.items():
        if count > 0:
            e = rules[rule]
            new_dict[rule[0] + e] += count
            new_dict[e + rule[1]] += count
            elements_count[e] += count
    rules_count = new_dict
    steps -= 1

counts = [x for x in elements_count.values()]
print(max(counts) - min(counts))