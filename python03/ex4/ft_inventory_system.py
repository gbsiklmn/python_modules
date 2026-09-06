#!/usr/bin/env python3
import sys

inventory = {}
for arg in sys.argv[1:]:

    parts = arg.split(':')
    if len(parts) != 2:
        print(f"Error - invalid parameter '{arg}'")
        continue

    name, qty_str = parts

    if name in inventory:
        print(f"Redundant item '{name}' - discarding")
        continue

    try:
        qty = int(qty_str)
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")
        continue

    inventory[name] = qty
