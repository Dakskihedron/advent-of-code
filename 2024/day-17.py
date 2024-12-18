# Part one
def run_program(reg, instr):
    reg_a = reg[0]
    reg_b = reg[1]
    reg_c = reg[2]

    instr_p = 0
    out = []
    while True:
        if instr_p >= len(instr):
            break

        combo = { 0: 0, 1: 1, 2: 2, 3: 3, 4: reg_a, 5: reg_b, 6: reg_c }

        # adv
        if instr[instr_p] == 0:
            reg_a = int(reg_a / (2 ** combo[instr[instr_p+1]]))
        # bxl
        elif instr[instr_p] == 1:
            reg_b = reg_b ^ instr[instr_p+1]
        # bst
        elif instr[instr_p] == 2:
            reg_b = combo[instr[instr_p+1]] % 8
        # jnz
        elif instr[instr_p] == 3:
            if reg_a != 0:
                instr_p = instr[instr_p+1]
                continue
        # bxc
        elif instr[instr_p] == 4:
            reg_b = reg_b ^ reg_c
        # out
        elif instr[instr_p] == 5:
            out.append(combo[instr[instr_p+1]] % 8)
        # bdv
        elif instr[instr_p] == 6:
            reg_b = int(reg_a / (2 ** combo[instr[instr_p+1]]))
        # cdv
        elif instr[instr_p] == 7:
            reg_c = int(reg_a / (2 ** combo[instr[instr_p+1]]))

        instr_p += 2

    print('Part one:', ','.join(map(str, out)))


# Part two
def find_lowest_reg_a_value(instr, reg):
    def out(reg_a):
        reg_b = reg_a % 8 # 2, 4
        reg_b = reg_b ^ 2 # 1, 2
        reg_c = int(reg_a / (2 ** reg_b)) # 7, 5
        reg_a = int(reg_a / (2 ** 3)) # 0, 3
        reg_b = reg_b ^ reg_c # 4, 7
        reg_b = reg_b ^ 7 # 1, 7
        return reg_b % 8 # 5, 5
    
    candidates = set()
    def recurse(instr, num):
        if len(instr) == 0:
            candidates.add(num)
            return

        for i in range(8):
            new_num = num << 3
            new_num += i
            if out(new_num) == instr[-1]:
                recurse(instr[:-1], new_num)

    recurse(instr, 0)
    print('Part two:', min(candidates))


def main():
    with open('inputs/day-17.in', 'r') as file:
        data = file.read().strip().split('\n')
    
    space = data.index('')
    reg = [int(_.split(' ')[2]) for _ in data[:space]]
    instr = list(map(int, data[space+1:][0].split(' ')[1].split(',')))

    run_program(reg, instr)
    find_lowest_reg_a_value(instr, reg)

if __name__ == '__main__':
    main()
