def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        # return f.read().strip()
        return [line.strip() for line in f.readlines()]


keypad = [
         ['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9'],
]


def part_one(inpt: list[str]) -> str:
    pos = [1, 1]
    result = ''
    for line in inpt:
        for move in line:
            new_pos = pos
            if move == 'U':
                new_pos = [pos[0] - 1, pos[1]]
            elif move == 'D':
                new_pos = [pos[0] + 1, pos[1]]
            elif move == 'L':
                new_pos = [pos[0], pos[1] - 1]
            elif move == 'R':
                new_pos = [pos[0], pos[1] + 1]

            if -1 < new_pos[0] < len(keypad) and -1 < new_pos[1] < len(keypad[0]):
                pos = new_pos

        result += keypad[pos[0]][pos[1]]

    return result


keypad2 = [
         ['', '',   '1', '',   ''],
         ['',  '2', '3', '4',  ''],
         ['5', '6', '7', '8', '9'],
         ['',  'A', 'B', 'C',  ''],
         ['',   '', 'D',  '',  ''],
]


def part_two(inpt: list[str]) -> str:
    pos = [2, 0]
    result = ''
    for line in inpt:
        for move in line:
            new_pos = pos
            if move == 'U':
                new_pos = [pos[0] - 1, pos[1]]
            elif move == 'D':
                new_pos = [pos[0] + 1, pos[1]]
            elif move == 'L':
                new_pos = [pos[0], pos[1] - 1]
            elif move == 'R':
                new_pos = [pos[0], pos[1] + 1]

            if -1 < new_pos[0] < len(keypad2) and -1 < new_pos[1] < len(keypad2[0])\
                    and keypad2[new_pos[0]][new_pos[1]] != '':
                pos = new_pos

        result += keypad2[pos[0]][pos[1]]

    return result


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example one: {part_one(inpt=input_string)}')
    print(f'Example two: {part_two(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
