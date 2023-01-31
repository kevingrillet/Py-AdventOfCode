import hashlib


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> str:
    result = ''
    cpt = 0
    while len(result) < 8:
        hash_md5 = hashlib.md5(f'{inpt}{cpt}'.encode('utf-8')).hexdigest()
        if hash_md5.startswith('00000'):
            result += hash_md5[5]
        cpt += 1

    return result


def part_two(inpt: str) -> str:
    result = [''] * 8
    cpt = 0
    found = 0
    while found < 8:
        hash_md5 = hashlib.md5(f'{inpt}{cpt}'.encode('utf-8')).hexdigest()
        if hash_md5.startswith('00000'):
            pos = hash_md5[5]
            if pos.isnumeric() and int(pos) < 8 and result[int(pos)] == '':
                result[int(pos)] = hash_md5[6]
                found += 1
        cpt += 1

    return ''.join(result)


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example one: {part_one(inpt=input_string)}')
    print(f'Example two: {part_two(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
