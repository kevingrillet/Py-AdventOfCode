def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def say(look: str) -> str:
    output = ""

    pos = 0
    cpt = 1
    while pos < len(look) - 1:
        if look[pos] == look[pos + 1]:
            cpt += 1
        else:
            output += '{}{}'.format(cpt, look[pos])
            cpt = 1
        pos += 1

    if look[-1] != look[-2]:
        output += '{}{}'.format('1', look[-1])

    return output


def process(inpt: str, times: int) -> str:
    look = inpt
    cycle = 0
    while cycle < times:
        # print(cycle, look)
        look = say(look)
        cycle += 1
    return look


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {len(process(inpt=input_string, times=40))}')
    print(f'Part two: {len(process(inpt=input_string, times=50))}')
