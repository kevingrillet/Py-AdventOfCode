from collections import defaultdict


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def run(inpt: list[str], a: int) -> int:
    registers = defaultdict(int)
    registers['a'] = a
    i = 0

    while i < len(inpt):
        # print(i, inpt[i], registers)
        splt = inpt[i].split(' ')
        if splt[0] == 'inc':
            registers[splt[1]] += 1
        elif splt[0] == 'dec':
            registers[splt[1]] -= 1
        elif splt[0] == 'jnz':
            v1 = registers[splt[1]] if splt[1].isalpha() else int(splt[1])
            if v1 != 0:
                i += registers[splt[2]] if splt[2].isalpha() else int(splt[2])
                continue
        elif splt[0] == 'cpy':
            if splt[2].isnumeric():
                print(i, inpt[i])
                i += 1
                continue
            if splt[1].isalpha():
                registers[splt[2]] = registers[splt[1]]
            else:
                registers[splt[2]] = int(splt[1])
        elif splt[0] == 'tgl':
            ii = i + (registers[splt[1]] if splt[1].isalpha() else int(splt[1]))
            if 0 <= ii < len(inpt):
                tmp = inpt[ii].split()
                if len(tmp) == 2:
                    tmp[0] = 'dec' if tmp[0] == 'inc' else 'inc'
                else:
                    tmp[0] = 'cpy' if tmp[0] == 'jnz' else 'jnz'
                inpt[ii] = ' '.join(tmp)
        i += 1
    return registers['a']


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {run(inpt=input_string, a=7)}')

    input_string = get_input(filename='input')
    print(f'Part one: {run(inpt=input_string.copy(), a=7)}')
    print(f'Part two: {run(inpt=input_string.copy(), a=12)}')
