#!/usr/bin/env python3
import random

PLAYERS = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab',
           'move', 'climb', 'swim', 'release', 'use']


def gen_event():
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield name, action

g = gen_event()

events = [next(g) for _ in range(10)]
print("Built list of 10 events:", events)
