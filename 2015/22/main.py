import time

# Spell costs and effects
MAGIC_MISSILE_COST = 53
MAGIC_MISSILE_DAMAGE = 4

DRAIN_COST = 73
DRAIN_DAMAGE = 2
DRAIN_HEAL = 2

SHIELD_COST = 113
SHIELD_DURATION = 6
SHIELD_ARMOR = 7

POISON_COST = 173
POISON_DURATION = 6
POISON_DAMAGE = 3

RECHARGE_COST = 229
RECHARGE_DURATION = 5
RECHARGE_MANA = 101


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def init_boss(inpt: list[str]) -> dict:
    boss = {"Hit Points": 100, "Damage": 0}
    for line in inpt:
        stat_name, stat_value = line.split(":")
        boss[stat_name] = int(stat_value)

    return boss


part_2 = False


def battle(
    player_hp: int,
    player_mana: int,
    boss_hp: int,
    boss_damage: int,
    shield_turns: int,
    poison_turns: int,
    recharge_turns: int,
    player_turn: bool,
    depth: int,
) -> int:
    # print('Depth:', str(depth).zfill(2),
    #       ';PlayerHP:', str(player_hp).zfill(3), ';PlayerMana:', str(player_mana).zfill(3),
    #       ';BossHP:', str(boss_hp).zfill(2), 'BossDmg:', str(boss_damage).zfill(2),
    #       ';ShieldTurns:', shield_turns, ';PoisonTurns:', poison_turns, ';RechargeTurns:', recharge_turns,
    #       ';PlayerTurn:', player_turn)

    if part_2 and player_turn:
        player_hp -= 1
    if depth == 0:
        raise NameError("Max depth")
    if boss_hp <= 0:
        return 0
    if player_hp <= 0:
        return 100000

    new_shield_turns = max(0, shield_turns - 1)
    new_poison_turns = max(0, poison_turns - 1)
    new_recharge_turns = max(0, recharge_turns - 1)

    if player_turn:
        if poison_turns > 0:
            boss_hp -= POISON_DAMAGE

        if boss_hp <= 0:
            return 0

        if recharge_turns > 0:
            player_mana += RECHARGE_MANA

        result = 100000

        if player_mana < MAGIC_MISSILE_COST:
            return result

        # Magic Missile
        if player_mana >= MAGIC_MISSILE_COST:
            new_player_mana = player_mana - MAGIC_MISSILE_COST
            new_boss_hp = boss_hp - MAGIC_MISSILE_DAMAGE
            result = min(
                result,
                MAGIC_MISSILE_COST
                + battle(
                    player_hp,
                    new_player_mana,
                    new_boss_hp,
                    boss_damage,
                    new_shield_turns,
                    new_poison_turns,
                    new_recharge_turns,
                    not player_turn,
                    depth - 1,
                ),
            )

        # Drain
        if player_mana >= DRAIN_COST:
            new_player_mana = player_mana - DRAIN_COST
            new_player_hp = player_hp + DRAIN_HEAL
            new_boss_hp = boss_hp - DRAIN_DAMAGE
            result = min(
                result,
                DRAIN_COST
                + battle(
                    new_player_hp,
                    new_player_mana,
                    new_boss_hp,
                    boss_damage,
                    new_shield_turns,
                    new_poison_turns,
                    new_recharge_turns,
                    not player_turn,
                    depth - 1,
                ),
            )

        # Shield
        if player_mana >= SHIELD_COST and new_shield_turns == 0:
            new_player_mana = player_mana - SHIELD_COST
            result = min(
                result,
                SHIELD_COST
                + battle(
                    player_hp,
                    new_player_mana,
                    boss_hp,
                    boss_damage,
                    SHIELD_DURATION,
                    new_poison_turns,
                    new_recharge_turns,
                    not player_turn,
                    depth - 1,
                ),
            )

        # Poison
        if player_mana >= POISON_COST and new_poison_turns == 0:
            new_player_mana = player_mana - POISON_COST
            result = min(
                result,
                POISON_COST
                + battle(
                    player_hp,
                    new_player_mana,
                    boss_hp,
                    boss_damage,
                    new_shield_turns,
                    POISON_DURATION,
                    new_recharge_turns,
                    not player_turn,
                    depth - 1,
                ),
            )

        # Recharge
        if player_mana >= RECHARGE_COST and new_recharge_turns == 0:
            new_player_mana = player_mana - RECHARGE_COST
            result = min(
                result,
                RECHARGE_COST
                + battle(
                    player_hp,
                    new_player_mana,
                    boss_hp,
                    boss_damage,
                    new_shield_turns,
                    new_poison_turns,
                    RECHARGE_DURATION,
                    not player_turn,
                    depth - 1,
                ),
            )

        return result
    else:
        if poison_turns > 0:
            boss_hp -= POISON_DAMAGE

        if recharge_turns > 0:
            player_mana += RECHARGE_MANA

        if boss_hp <= 0:
            return 0
        else:
            player_hp -= max(1, boss_damage - (0 if shield_turns == 0 else SHIELD_ARMOR))

        return battle(
            player_hp,
            player_mana,
            boss_hp,
            boss_damage,
            new_shield_turns,
            new_poison_turns,
            new_recharge_turns,
            not player_turn,
            depth - 1,
        )


def example() -> int:
    return battle(10, 250, 13, 8, 0, 0, 0, True, 25)


def example2() -> int:
    return battle(50, 500, 13, 14, 0, 0, 0, True, 25)


def part_one(inpt: list[str]) -> int:
    boss = init_boss(inpt)
    return battle(50, 500, boss["Hit Points"], boss["Damage"], 0, 0, 0, True, 100)


def part_two(inpt: list[str]) -> int:
    global part_2
    part_2 = True
    return part_one(inpt)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    # print(f'Example one: {example()}')
    # print(f'Example two: {example2()}')
    st = time.time()
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Execution time: {time.time() - st} seconds")
    st = time.time()
    print(f"Part two: {part_two(inpt=input_string)}")
    print(f"Execution time: {time.time() - st} seconds")
