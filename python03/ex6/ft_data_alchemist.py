#!/usr/bin/env python3

import random

names = ['Alice', 'bob', 'Charlie', 'dylan',
         'Emma', 'Gregory', 'john', 'kevin', 'Liam']
capitalized = [n.capitalize() for n in names]
already_capitalized = [n for n in names if n == n.capitalize()]
score_dict = {n: random.randint(50, 1000) for n in capitalized}
average = round(sum(score_dict.values()) / len(score_dict.values()), 2)
high_scores = {in score_dict.items() if score_dict.values() > average}

print("=== Game Data Alchemist ===")

print(f"Initial list of players: {names}")
print(f"New list with all names capitalized: {capitalized}")
print(f"New list of capitalized names only: {already_capitalized}")
print(f"Score dict: {score_dict}")
print(f"Score average is {average}")
print(f"High scores: {high_scores}")
