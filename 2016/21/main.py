from itertools import permutations


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def run(inpt: list[str], password: str, direction: int = 1) -> str:
    pwd = list(password)
    for line in inpt[::direction]:
        splt = line.split()
        if line.startswith('move'):
            pwd.insert(int(splt[-1]), pwd.pop(int(splt[2])))
        elif line.startswith('swap'):
            x, y = splt[2], splt[-1]
            if splt[1] == 'position':
                x, y = int(x), int(y)
            else:
                x, y = pwd.index(x), pwd.index(y)
            pwd[x], pwd[y] = pwd[y], pwd[x]
        elif line.startswith('rotate'):
            if splt[1] == 'based':
                x = pwd.index(splt[-1])
                if direction == 1:
                    if x >= 4:
                        x += 1
                    x %= len(pwd)
                else:
                    pass
                    # TODO
                for _ in range(x + 1):
                    pwd.insert(0, pwd.pop(-1))
            elif (splt[1] == 'left' and direction == 1) or (splt[1] == 'right' and direction == -1):
                x = int(splt[2])
                x %= len(pwd)
                for _ in range(x):
                    pwd.append(pwd.pop(0))
            elif (splt[1] == 'right' and direction == 1) or (splt[1] == 'left' and direction == -1):
                x = int(splt[2])
                x %= len(pwd)
                for _ in range(x):
                    pwd.insert(0, pwd.pop(-1))
        elif line.startswith('reverse'):
            x, y = int(splt[2]), int(splt[-1]) + 1
            if direction == -1:
                x, y = y, x
            pwd[x:y] = pwd[x:y][::-1]

    return ''.join(pwd)


def bruteforce(inpt: list[str], output: str) -> str:
    for perm in permutations(output):
        if run(inpt, perm) == output:
            return ''.join(perm)


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {run(inpt=input_string, password="abcde")}')

    input_string = get_input(filename='input')
    print(f'Part one: {run(inpt=input_string, password="abcdefgh")}')
    print(f'Part two (bf): {bruteforce(inpt=input_string, output="fbgdceah")}')
    print(f'Part two (wip): {run(inpt=input_string, password="fbgdceah", direction=-1)}')
