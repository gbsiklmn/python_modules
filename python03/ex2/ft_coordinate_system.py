#!/usr/bin/env python3
import math


def get_player_pos():
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            parts = raw.split(',')
            x, y, z = parts           
            return x, y, z

        except ValueError:
            print("Invalid syntax")

        for p in parts:
            try:
                x, y, z, = float(x), float(y), float(z)
                return(x, y, z)
            except:
                print(f"Error on parameter '{p}': {e}")


print("=== Game Coordinate System ===")
print("Get a first set of coordinates")
pos1 = get_player_pos()
print("Got a first tuple:", pos1)
x, y, z = pos1
print(f"It includes: X={x}, Y={y}, Z={z}")
dist_to_center = round(math.sqrt(x**2 + y**2 + z**2), 4)
print(f"Distance to center: {dist_to_center}")
print("Get a second set of coordinates")
pos2 = get_player_pos()
a, b, c = pos2
dist_between = round(math.sqrt((a-x)**2 + (b-y)**2 + (c-z)**2), 4)
print(f"Distance between the 2 sets of coordinates: {dist_between}")
