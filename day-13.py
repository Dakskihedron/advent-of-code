import ast

with open('inputs/day-13.txt', 'r') as file:
    data = file.read().strip()


# Part one
packets = data.strip().split('\n\n')
packets = [x.split('\n') for x in packets]
packets = [[ast.literal_eval(y) for y in x] for x in packets]

def compare(left, right):
    # If both items are lists
    if isinstance(left, list) and isinstance(right, list):
        x, y = max([len(left), len(right)]), min([len(left), len(right)])
        for i in range(x):
            # If one list runs out of items
            if i == y:
                return len(left) < len(right)

            # Compare items
            result = compare(left[i], right[i])
            if result is None:
                continue
            else:
                return result
            
        return None

    # If both items are integers
    elif isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right

    # If mixed item types
    else:
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return compare(left, right)

ordered_sum = 0
for p in range(len(packets)):
    left, right = packets[p][0], packets[p][1]
    if compare(left, right):
        ordered_sum += (p + 1)
print('Part 1:', ordered_sum)


# Part two
packets = data.strip().split('\n')
packets = [x for x in packets if x != '']
packets = [ast.literal_eval(x) for x in packets]

divider1_before = 1
divider2_before = 2
for packet in packets:
    if compare(packet, [[2]]):
        divider1_before += 1
    if compare(packet, [[6]]):
        divider2_before += 1

print('Part 2:', divider1_before * divider2_before)