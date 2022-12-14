def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


shop = {
    'weapon': {'dagger': [8, 4, 0], 'shortsword': [10, 5, 0], 'warhammer': [25, 6, 0], 'longsword': [40, 7, 0],
               'greataxe': [74, 8, 0]},
    'armour': {'leather': [13, 0, 1], 'chainmail': [31, 0, 2], 'splintmail': [53, 0, 3], 'bandedmail': [75, 0, 4],
               'platemail': [102, 0, 5]},
    'rings': {'damage1': [25, 1, 0], 'damage2': [50, 2, 0], 'damage3': [100, 3, 0], 'defense1': [20, 0, 1],
              'defense2': [40, 0, 2], 'defense3': [80, 0, 3]}
}

boss = {
    'Hit Points': 100,
    'Damage': 0,
    'Armor': 0
}


def init_boss(inpt: list[str]) -> None:
    for line in inpt:
        stat_name, stat_value = line.split(':')
        boss[stat_name] = int(stat_value)


def init_shop() -> None:
    # Add 2 "empty" slots for further loop
    shop['armour']['None'] = [0, 0, 0]
    shop['rings']['None'] = [0, 0, 0]


def battle(weapon: str, armour: str = None, ring_1: str = None, ring_2: str = None) -> int:
    boss_stats = boss.copy()
    player_stats = {
        'Hit Points': 100,
        'Damage': 0,
        'Armor': 0
    }
    cost = 0

    if weapon:
        cost += shop['weapon'][weapon][0]
        player_stats['Damage'] += shop['weapon'][weapon][1]
        player_stats['Armor'] += shop['weapon'][weapon][2]

    if armour:
        cost += shop['armour'][armour][0]
        player_stats['Damage'] += shop['armour'][armour][1]
        player_stats['Armor'] += shop['armour'][armour][2]

    if ring_1:
        cost += shop['rings'][ring_1][0]
        player_stats['Damage'] += shop['rings'][ring_1][1]
        player_stats['Armor'] += shop['rings'][ring_1][2]

    if ring_2:
        cost += shop['rings'][ring_2][0]
        player_stats['Damage'] += shop['rings'][ring_2][1]
        player_stats['Armor'] += shop['rings'][ring_2][2]

    while True:
        boss_stats['Hit Points'] -= player_stats['Damage'] - boss_stats['Armor']
        if boss_stats['Hit Points'] <= 0:
            return cost

        player_stats['Hit Points'] -= boss_stats['Damage'] - player_stats['Armor']
        if player_stats['Hit Points'] <= 0:
            # Negative because lost, and easy to use later :)
            return cost * -1


def part_one() -> int:
    result = 1000

    for weapon in shop['weapon']:
        battle_result = battle(weapon)
        if -1 < battle_result < result:
            result = battle_result

        for armour in shop['armour']:
            battle_result = battle(weapon, armour)
            if -1 < battle_result < result:
                result = battle_result

            for ring_1 in shop['rings']:
                battle_result = battle(weapon, armour, ring_1)
                if -1 < battle_result < result:
                    result = battle_result

                for ring_2 in shop['rings']:
                    battle_result = battle(weapon, armour, ring_1, ring_2)
                    if -1 < battle_result < result:
                        result = battle_result

    return result


def part_two() -> int:
    result = 0

    for weapon in shop['weapon']:
        battle_result = battle(weapon)
        if battle_result * -1 > result:
            result = battle_result * -1

        for armour in shop['armour']:
            battle_result = battle(weapon, armour)
            if battle_result * -1 > result:
                result = battle_result * -1

            for ring_1 in shop['rings']:
                battle_result = battle(weapon, armour, ring_1)
                if battle_result * -1 > result:
                    result = battle_result * -1

                for ring_2 in shop['rings']:
                    battle_result = battle(weapon, armour, ring_1, ring_2)
                    if battle_result * -1 > result:
                        result = battle_result * -1

    return result


if __name__ == '__main__':
    input_string = get_input(filename='input')
    init_boss(input_string)
    init_shop()

    print(f'Part one: {part_one()}')
    print(f'Part two: {part_two()}')
