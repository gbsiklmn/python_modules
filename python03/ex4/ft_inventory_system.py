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

print("Got inventory:", inventory)
item_list = list(inventory.keys())
print(f"Item list: {item_list}")
total_qty = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total_qty}")

for name, qty in inventory.items():
    pct = round(qty / total_qty * 100, 1)
    print(f"Item {name} represents {pct}%")

most_name, most_qty = None, None
for name, qty in inventory.items():
    if most_qty is None or qty > most_qty:
        most_name, most_qty = name, qty

inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
print(f"Item most abundant: {most_name} with quantity {most_qty}")