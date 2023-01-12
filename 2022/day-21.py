from sympy.solvers import solve
from sympy import Symbol

with open('inputs/day-21.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = { x.split(':')[0].strip():x.split(':')[1].strip() for x in data }
    data = { _:int(v) if v.isdigit() else tuple(v.split(' ')) for _,v in data.items() }


# Part one
def calc_root(equ_dict, key):
    equ = equ_dict[key]

    if isinstance(equ, tuple):
        num1, op, num2 = equ
        result_equ = f"calc_root(equ_dict, '{num1}') {op} calc_root(equ_dict, '{num2}')"
        return int(eval(result_equ))

    elif isinstance(equ, int):
        return equ

print('Part 1:', calc_root(data, 'root'))


# Part two
def gen_equ(equ_dict, key):
    equ = equ_dict[key]

    if key == 'root':
        num1, _, num2 = equ
        num1 = gen_equ(equ_dict, num1)
        num2 = gen_equ(equ_dict, num2)
        return f"{num1} - {num2}"

    if isinstance(equ, tuple):
        num1, op, num2 = equ
        result_equ = f"({gen_equ(equ_dict, num1)} {op} {gen_equ(equ_dict, num2)})"
        return result_equ

    elif isinstance(equ, int) or equ == 'x':
        return equ


data['humn'] = 'x'
equ = gen_equ(data, 'root')
x = Symbol('x')
print('Part 2:', round(solve(eval(equ), x)[0]))
