#!/usr/bin/env python3
import random
from typing import Generator

PLAYERS = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab',
           'move', 'climb', 'swim', 'release', 'use']


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield name, action

print("=== Game Data Stream Processor ===")
g = gen_event()

for i in range(1000):
    name, action = next(g)
    print(f"Event {i}: Player {name} did action {action}")

events = [next(g) for _ in range(10)]
print("Built list of 10 events:", events)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event


for event in consume_event(events):
    print("Got event from list:", event)
    print("Remains in list:", events)
