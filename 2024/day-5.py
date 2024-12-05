from collections import defaultdict

# Part one
def sum_of_middle_pages(rules, updates):
    sum = 0

    for i in range(len(updates)):
        for j in range(len(updates[i])):
            page = updates[i][j]
            before = rules[page]
            if len(set(before).intersection(updates[i][j+1:])) != 0:
                break
            
            if j == len(updates[i]) - 1:
                sum += updates[i][len(updates[i]) // 2]

    print('Part one:', sum)


# Part two
def sum_of_middle_pages_in_corrected(rules, updates):
    sum = 0

    incorrect = []
    for i in range(len(updates)):
        for j in range(len(updates[i])):
            page = updates[i][j]
            before = rules[page]
            if len(set(before).intersection(updates[i][j+1:])) != 0:
                incorrect.append(updates[i])
                break

    for i in range(len(incorrect)):
        unsorted = incorrect[i]
        while True:
            sorts = 0
            for j in range(1, len(unsorted)):
                x = unsorted[j-1]
                y = unsorted[j]
                if y in rules[x]:
                    unsorted[j-1], unsorted[j] = unsorted[j], unsorted[j-1]
                    sorts += 1

            if sorts == 0:
                sum += unsorted[len(unsorted) // 2]
                break

    print('Part two:', sum)


def main():
    with open('inputs/day-5.in', 'r') as file:
        data = file.read().strip().split('\n')
        space = data.index('')
        rules, updates = data[:space], data[space+1:]

        rules_dict = defaultdict(list)
        for rule in rules:
            before, after = map(int, rule.split('|'))
            rules_dict[after].append(before)

        updates = [list(map(int, _.split(','))) for _ in updates]

    sum_of_middle_pages(rules_dict, updates)
    sum_of_middle_pages_in_corrected(rules_dict, updates)

if __name__ == '__main__':
    main()