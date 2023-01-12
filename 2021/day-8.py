with open('inputs/day-8.txt') as file:
    data = file.read().split('\n')
    data = [x.split('|') for x in data]

# Part one
uniques = 0
for x in data:
    for y in x[1].split():
        if len(y) in [2, 3, 4, 7]:
            uniques += 1

print(uniques)

# Part two
def split(word):
    return [x for x in word]

total = 0
for line in data:
    display_codes = {}
    for code in line[0].split():
        if code not in display_codes:
            if len(code) == 2:
                display_codes['1'] = code
            elif len(code) == 4:
                display_codes['4'] = code
            elif len(code) == 3:
                display_codes['7'] = code
            elif len(code) == 7:
                display_codes['8'] = code

    # Get 3
    for code in line[0].split():
        if code not in display_codes.values() and len(code) == 5:
            if set(split(display_codes['7'])).issubset(set(code)):
                display_codes['3'] = code

    # Get 9
    for code in line[0].split():
        if code not in display_codes.values() and len(code) == 6:
            if set(split(display_codes['3'])).issubset(set(split(code))):
                display_codes['9'] = code

    # Get 5 and 2
    for code in line[0].split():
        if code not in display_codes.values() and len(code) == 5:
            if len(set(split(code)).difference(set(split(display_codes['4'])))) == 2:
                display_codes['5'] = code
    for code in line[0].split():
        if code not in display_codes.values() and len(code) == 5:
            display_codes['2'] = code

    # Get 0 and 6
    for code in line[0].split():
        if code not in display_codes.values() and len(code) == 6:
            if set(split(display_codes['7'])).issubset(set(split(code))):
                display_codes['0'] = code
    for code in line[0].split():
        if code not in display_codes.values():
            display_codes['6'] = code

    output = ''
    for code in line[1].split():
        for key, item in display_codes.items():
            if ''.join(sorted(code)) == ''.join(sorted(item)):
                output += key
    total += int(output)

print(total)