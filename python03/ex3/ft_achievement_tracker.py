#!/usr/bin/env python3
import random

ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder',
]


def gen_player_achievements():
    count = random.randint(3, 9)
    return set(random.sample(ACHIEVEMENTS, count))



print("=== Achievement Tracker System ===")
alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

print("Player Alice:", alice)
print("Player Bob:", bob)
print("Player Charlie:", charlie)
print("Player Dylan:", dylan)
distinct = alice | bob | charlie | dylan
common = alice & bob & charlie & dylan
print("\nAll distinct achievements:", distinct)
print("\nCommon achievements:", common)
all_achievements = set(ACHIEVEMENTS)
only_alice = alice - (bob | charlie | dylan)
only_bob = bob - (alice | charlie | dylan)
only_charlie = charlie - (alice | bob | dylan)
only_dylan = dylan - (alice | bob | charlie)

print("\nOnly Alice has:", only_alice)
print("Only Bob has:", only_bob)
print("Only Charlie has:", only_charlie)
print("Only Dylan has:", only_dylan)

alice_missing = all_achievements - alice
bob_missing = all_achievements - bob
charlie_missing = all_achievements - charlie
dylan_missing = all_achievements - dylan

print("\nAlice is missing:", alice_missing)
print("Bob is missing:", bob_missing)
print("Charlie is missing:", charlie_missing)
print("Dylan is missing:", dylan_missing)
