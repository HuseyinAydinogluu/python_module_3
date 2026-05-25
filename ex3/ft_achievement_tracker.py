import random

ALL_ACHIEVEMENTS = [
    "First Steps",
    "Boss Slayer",
    "Treasure Hunter",
    "Master Explorer",
    "Crafting Genius",
    "Collector Supreme",
    "Speed Runner",
    "Untouchable",
    "World Savior",
    "Strategist",
    "Sharp Mind",
    "Hidden Path Finder",
    "Unstoppable",
    "Survivor"
]

def gen_player_achievements():
    number_of_achievements = random.randint(5, 9)

    random_achievements = random.sample( ALL_ACHIEVEMENTS, number_of_achievements)
    return set(random_achievements)

print(f" === Achievement Tracker System ===")

alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print(f"Player Alice:", alice)
print(f"Player Bob:", bob)
print(f"Player Charlie:", charlie)
print(f"Player Dylan:", dylan)

all_achievements = (
    alice
    .union(bob)
    .union(charlie)
    .union(dylan)
)
print(f"All distinct achievements:", all_achievements)

common_achievements = (
    alice
    .intersection(bob)
    .intersection(charlie)
    .intersection(dylan)
)
print(f"Common achievements:", common_achievements)

only_alice = alice.difference(bob.union(charlie).union(dylan))

only_bob = bob.difference(
    alice.union(charlie).union(dylan)
)

only_charlie = charlie.difference(
    alice.union(bob).union(dylan)
)

only_dylan = dylan.difference(
    alice.union(bob).union(charlie)
)

print("Only Alice has:", only_alice)
print("Only Bob has:", only_bob)
print("Only Charlie has:", only_charlie)
print("Only Dylan has:", only_dylan)

alice_missing = all_achievements.difference(alice)
bob_missing = all_achievements.difference(bob)
charlie_missing = all_achievements.difference(charlie)
dylan_missing = all_achievements.difference(dylan)


print("Alice is missing:", alice_missing)
print("Bob is missing:", bob_missing)
print("Charlie is missing:", charlie_missing)
print("Dylan is missing:", dylan_missing)