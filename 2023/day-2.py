# Part one and two
def calc_games(data):
    id_sum = 0
    power_sum = 0

    for line in data:
        line = line.split(':')
        game_id = int(line[0].strip().split(' ')[1])
        counts = {'red': 0, 'green': 0, 'blue': 0}
        line = line[1].split(';')

        for subset in line:
            subset = subset.split(',')
            for pair in subset:
                pair = pair.strip().split(' ')
                count = int(pair[0])
                colour = pair[1]

                if count > counts[colour]:
                    counts[colour] = count

        if counts['red'] <= 12 and counts['green'] <= 13 and counts['blue'] <= 14:
            id_sum += game_id
        
        power_sum += counts['red'] * counts['green'] * counts['blue']
    
    print('Part one:', id_sum)
    print('Part two:', power_sum)


def main():
    with open('inputs/day-2.in', 'r') as file:
        data = file.read().strip().split('\n')
    calc_games(data)


if __name__ == '__main__':
    main()