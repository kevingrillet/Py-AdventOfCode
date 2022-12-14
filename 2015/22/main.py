import time


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def init_boss(inpt: list[str]) -> dict:
    boss = {
        'Hit Points': 100,
        'Damage': 0
    }
    for line in inpt:
        stat_name, stat_value = line.split(':')
        boss[stat_name] = int(stat_value)

    return boss


part_2 = False


def battle(player_hp: int, player_mana: int, boss_hp: int, boss_damage: int, shield_turns: int, poison_turns: int,
           recharge_turns: int, player_turn: bool, depth: int) -> int:
    # print('Depth:', str(depth).zfill(2),
    #       ';PlayerHP:', str(player_hp).zfill(3), ';PlayerMana:', str(player_mana).zfill(3),
    #       ';BossHP:', str(boss_hp).zfill(2), 'BossDmg:', str(boss_damage).zfill(2),
    #       ';ShieldTurns:', shield_turns, ';PoisonTurns:', poison_turns, ';RechargeTurns:', recharge_turns,
    #       ';PlayerTurn:', player_turn)

    if part_2 and player_turn:
        player_hp -= 1
    if depth == 0:
        raise NameError('Max depth')
    if boss_hp <= 0:
        return 0
    if player_hp <= 0:
        return 100000

    new_shield_turns = max(0, shield_turns - 1)
    new_poison_turns = max(0, poison_turns - 1)
    new_recharge_turns = max(0, recharge_turns - 1)

    if player_turn:
        if poison_turns > 0:
            boss_hp -= 3

        if boss_hp <= 0:
            return 0

        if recharge_turns > 0:
            player_mana += 101

        result = 100000

        if player_mana < 53:
            return result

        # Magic Missile
        if player_mana >= 53:
            new_player_mana = player_mana - 53
            new_boss_hp = boss_hp - 4
            result = min(result, 53 + battle(player_hp, new_player_mana, new_boss_hp, boss_damage, new_shield_turns,
                                             new_poison_turns, new_recharge_turns, not player_turn, depth - 1))

        # Drain
        if player_mana >= 73:
            new_player_mana = player_mana - 73
            new_player_hp = player_hp + 2
            new_boss_hp = boss_hp - 2
            result = min(result, 73 + battle(new_player_hp, new_player_mana, new_boss_hp, boss_damage, new_shield_turns,
                                             new_poison_turns, new_recharge_turns, not player_turn, depth - 1))

        # Shield
        if player_mana >= 113 and new_shield_turns == 0:
            new_player_mana = player_mana - 113
            result = min(result, 113 + battle(player_hp, new_player_mana, boss_hp, boss_damage, 6, new_poison_turns,
                                              new_recharge_turns, not player_turn, depth - 1))

        # Poison
        if player_mana >= 173 and new_poison_turns == 0:
            new_player_mana = player_mana - 173
            result = min(result, 173 + battle(player_hp, new_player_mana, boss_hp, boss_damage, new_shield_turns, 6,
                                              new_recharge_turns, not player_turn, depth - 1))

        # Recharge
        if player_mana >= 229 and new_recharge_turns == 0:
            new_player_mana = player_mana - 229
            result = min(result, 229 + battle(player_hp, new_player_mana, boss_hp, boss_damage, new_shield_turns,
                                              new_poison_turns, 5, not player_turn, depth - 1))

        return result
    else:
        if poison_turns > 0:
            boss_hp -= 3

        if recharge_turns > 0:
            player_mana += 101

        if boss_hp <= 0:
            return 0
        else:
            player_hp -= max(1, boss_damage - (0 if shield_turns == 0 else 7))

        return battle(player_hp, player_mana, boss_hp, boss_damage, new_shield_turns, new_poison_turns,
                      new_recharge_turns, not player_turn, depth - 1)


def example() -> int:
    return battle(10, 250, 13, 8, 0, 0, 0, True, 25)


def example2() -> int:
    return battle(50, 500, 13, 14, 0, 0, 0, True, 25)


def part_one(inpt: list[str]) -> int:
    boss = init_boss(inpt)
    return battle(50, 500, boss['Hit Points'], boss['Damage'], 0, 0, 0, True, 100)


def part_two(inpt: list[str]) -> int:
    global part_2
    part_2 = True
    return part_one(inpt)


if __name__ == '__main__':
    input_string = get_input(filename='input')
    # print(f'Example one: {example()}')
    # print(f'Example two: {example2()}')
    st = time.time()
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Execution time: {time.time() - st} seconds')
    st = time.time()
    print(f'Part two: {part_two(inpt=input_string)}')
    print(f'Execution time: {time.time() - st} seconds')
