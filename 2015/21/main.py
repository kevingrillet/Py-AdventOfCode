import itertools


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


SHOP = {
    "weapon": {
        "dagger": [8, 4, 0],
        "shortsword": [10, 5, 0],
        "warhammer": [25, 6, 0],
        "longsword": [40, 7, 0],
        "greataxe": [74, 8, 0],
    },
    "armour": {
        "None": [0, 0, 0],
        "leather": [13, 0, 1],
        "chainmail": [31, 0, 2],
        "splintmail": [53, 0, 3],
        "bandedmail": [75, 0, 4],
        "platemail": [102, 0, 5],
    },
    "rings": {
        "None1": [0, 0, 0],
        "None2": [0, 0, 0],
        "damage1": [25, 1, 0],
        "damage2": [50, 2, 0],
        "damage3": [100, 3, 0],
        "defense1": [20, 0, 1],
        "defense2": [40, 0, 2],
        "defense3": [80, 0, 3],
    },
}

BOSS = {}


def init_boss(inpt: list[str]) -> None:
    for line in inpt:
        stat_name, stat_value = line.split(":")
        BOSS[stat_name] = int(stat_value)


def battle(equipment: list[list[int]]) -> tuple[bool, int]:
    """Simulate battle and return (player_wins, cost)."""
    boss_hp = BOSS["Hit Points"]
    player_hp = 100
    cost = sum(item[0] for item in equipment)
    player_damage = sum(item[1] for item in equipment)
    player_armor = sum(item[2] for item in equipment)

    while True:
        boss_hp -= max(1, player_damage - BOSS["Armor"])
        if boss_hp <= 0:
            return True, cost

        player_hp -= max(1, BOSS["Damage"] - player_armor)
        if player_hp <= 0:
            return False, cost


def solve() -> tuple[int, int]:
    """Find minimum cost to win and maximum cost to lose."""
    min_cost_to_win = float("inf")
    max_cost_to_lose = 0

    # Generate all equipment combinations
    for weapon in SHOP["weapon"].values():
        for armour in SHOP["armour"].values():
            for ring1, ring2 in itertools.combinations(SHOP["rings"].values(), 2):
                equipment = [weapon, armour, ring1, ring2]
                won, cost = battle(equipment)

                if won:
                    min_cost_to_win = min(min_cost_to_win, cost)
                else:
                    max_cost_to_lose = max(max_cost_to_lose, cost)

    return int(min_cost_to_win), max_cost_to_lose


def part_one(inpt: list[str]) -> int:
    init_boss(inpt)
    min_cost, _ = solve()
    return min_cost


def part_two(inpt: list[str]) -> int:
    init_boss(inpt)
    _, max_cost = solve()
    return max_cost


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(input_string)}")
    print(f"Part two: {part_two(input_string)}")
