# Part one
def find_all_xmas(data):
    data = [[_ for _ in _] for _ in data]

    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):

            if data[i][j] != 'X':
                continue

            if i > 2:
                # Top
                if ''.join([data[i-x][j] for x in range(1,4)]) == 'MAS':
                    sum += 1

                # Top-left
                if j > 2 and ''.join([data[i-x][j-x] for x in range(1,4)]) == 'MAS':
                    sum += 1

                # Top-right
                if j < (len(data[i]) - 3) and ''.join([data[i-x][j+x] for x in range(1,4)]) == 'MAS':
                    sum += 1

            if i < (len(data) - 3):
                # Bottom
                if ''.join([data[i+x][j] for x in range(1,4)]) == 'MAS':
                    sum += 1

                # Bottom-left
                if j > 2 and ''.join([data[i+x][j-x] for x in range(1,4)]) == 'MAS':
                    sum += 1

                # Bottom-right
                if j < (len(data[i]) - 3) and ''.join([data[i+x][j+x] for x in range(1,4)]) == 'MAS':
                    sum += 1

            # Left
            if j > 2 and ''.join([data[i][j-x] for x in range(1,4)]) == 'MAS':
                sum += 1

            # Right
            if j < (len(data[i]) - 3) and ''.join([data[i][j+x] for x in range(1,4)]) == 'MAS':
                sum += 1

    print('Part one:', sum)


# Part two
def find_all_x_mas(data):
    data = [[_ for _ in _] for _ in data]

    sum = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):

            if data[i][j] != 'A':
                continue

            m_count = 0
            s_count = 0

            for m in [-1,1]:
                for n in [-1, 1]:
                    val = data[i+m][j+n]
                    if val == 'M':
                        m_count += 1
                    elif val == 'S':
                        s_count += 1
            
            if m_count == 2 and s_count == 2:
                if (data[i-1][j-1] != data[i+1][j+1]) and (data[i-1][j+1] != data[i+1][j-1]):
                    sum += 1

    print('Part two:', sum)


def main():
    with open('inputs/day-4.in', 'r') as file:
        data = file.read().strip().split('\n')

    find_all_xmas(data)
    find_all_x_mas(data)

if __name__ == '__main__':
    main()