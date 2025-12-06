from dataclasses import dataclass

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


@dataclass
class GameState:
    player_hp: int
    player_mana: int
    boss_hp: int
    boss_damage: int
    shield_turns: int = 0
    poison_turns: int = 0
    recharge_turns: int = 0

    def apply_effects(self) -> None:
        """Apply ongoing effects and decrease their duration."""
        if self.poison_turns > 0:
            self.boss_hp -= POISON_DAMAGE
            self.poison_turns -= 1

        if self.recharge_turns > 0:
            self.player_mana += RECHARGE_MANA
            self.recharge_turns -= 1

        if self.shield_turns > 0:
            self.shield_turns -= 1

    @property
    def armor(self) -> int:
        return SHIELD_ARMOR if self.shield_turns > 0 else 0


def battle(state: GameState, player_turn: bool, depth: int, hard_mode: bool = False) -> int:
    if depth == 0:
        return 100000

    if hard_mode and player_turn:
        state.player_hp -= 1
        if state.player_hp <= 0:
            return 100000

    state.apply_effects()

    if state.boss_hp <= 0:
        return 0

    if not player_turn:
        # Boss turn
        state.player_hp -= max(1, state.boss_damage - state.armor)
        if state.player_hp <= 0:
            return 100000
        return battle(state, True, depth - 1, hard_mode)

    # Player turn - try all possible spells
    if state.player_mana < MAGIC_MISSILE_COST:
        return 100000

    min_cost = 100000

    # Try Magic Missile
    if state.player_mana >= MAGIC_MISSILE_COST:
        new_state = GameState(
            state.player_hp,
            state.player_mana - MAGIC_MISSILE_COST,
            state.boss_hp - MAGIC_MISSILE_DAMAGE,
            state.boss_damage,
            state.shield_turns,
            state.poison_turns,
            state.recharge_turns,
        )
        min_cost = min(min_cost, MAGIC_MISSILE_COST + battle(new_state, False, depth - 1, hard_mode))

    # Try Drain
    if state.player_mana >= DRAIN_COST:
        new_state = GameState(
            state.player_hp + DRAIN_HEAL,
            state.player_mana - DRAIN_COST,
            state.boss_hp - DRAIN_DAMAGE,
            state.boss_damage,
            state.shield_turns,
            state.poison_turns,
            state.recharge_turns,
        )
        min_cost = min(min_cost, DRAIN_COST + battle(new_state, False, depth - 1, hard_mode))

    # Try Shield
    if state.player_mana >= SHIELD_COST and state.shield_turns == 0:
        new_state = GameState(
            state.player_hp,
            state.player_mana - SHIELD_COST,
            state.boss_hp,
            state.boss_damage,
            SHIELD_DURATION,
            state.poison_turns,
            state.recharge_turns,
        )
        min_cost = min(min_cost, SHIELD_COST + battle(new_state, False, depth - 1, hard_mode))

    # Try Poison
    if state.player_mana >= POISON_COST and state.poison_turns == 0:
        new_state = GameState(
            state.player_hp,
            state.player_mana - POISON_COST,
            state.boss_hp,
            state.boss_damage,
            state.shield_turns,
            POISON_DURATION,
            state.recharge_turns,
        )
        min_cost = min(min_cost, POISON_COST + battle(new_state, False, depth - 1, hard_mode))

    # Try Recharge
    if state.player_mana >= RECHARGE_COST and state.recharge_turns == 0:
        new_state = GameState(
            state.player_hp,
            state.player_mana - RECHARGE_COST,
            state.boss_hp,
            state.boss_damage,
            state.shield_turns,
            state.poison_turns,
            RECHARGE_DURATION,
        )
        min_cost = min(min_cost, RECHARGE_COST + battle(new_state, False, depth - 1, hard_mode))

    return min_cost


def init_boss(inpt: list[str]) -> dict:
    boss = {}
    for line in inpt:
        stat_name, stat_value = line.split(":")
        boss[stat_name] = int(stat_value)
    return boss


def part_one(inpt: list[str]) -> int:
    boss = init_boss(inpt)
    state = GameState(50, 500, boss["Hit Points"], boss["Damage"])
    return battle(state, True, 100, False)


def part_two(inpt: list[str]) -> int:
    boss = init_boss(inpt)
    state = GameState(50, 500, boss["Hit Points"], boss["Damage"])
    return battle(state, True, 100, True)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
