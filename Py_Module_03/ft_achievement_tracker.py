import random


ALL_ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Speed Runner",
    "Treasure Hunter",
    "Master Explorer",
    "World Savior",
    "Survivor",
    "Unstoppable",
    "Untouchable",
    "Strategist",
    "Crafting Genius",
    "Collector Supreme",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(6, 10)
    selected = random.sample(ALL_ACHIEVEMENTS, amount)
    selected_set = set(selected)

    return selected_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    print("Player Alice:", alice)

    bob = gen_player_achievements()
    print("Player Bob:", bob)

    charlie = gen_player_achievements()
    print("Player Charlie:", charlie)

    dylan = gen_player_achievements()
    print("Player Dylan:", dylan)
    print()

    all_distinct = alice.union(bob, charlie, dylan)
    print("All distinct achievements:", all_distinct)
    print()

    common = alice.intersection(bob, charlie, dylan)
    print("Common achievements:", common)
    print()

    only_alice = alice.difference(bob, charlie, dylan)
    print("Only Alice has:", only_alice)

    only_bob = bob.difference(alice, charlie, dylan)
    print("Only Bob has:", only_bob)

    only_charlie = charlie.difference(alice, bob, dylan)
    print("Only Charlie has:", only_charlie)

    only_dylan = dylan.difference(alice, bob, charlie)
    print("Only Dylan has:", only_dylan)
    print()

    achievement_catalog = set(ALL_ACHIEVEMENTS)

    alice_missing = achievement_catalog.difference(alice)
    print("Alice is missing:", alice_missing)

    bob_missing = achievement_catalog.difference(bob)
    print("Bob is missing:", bob_missing)

    charlie_missing = achievement_catalog.difference(charlie)
    print("Charlie is missing:", charlie_missing)

    dylan_missing = achievement_catalog.difference(dylan)
    print("Dylan is missing:", dylan_missing)
