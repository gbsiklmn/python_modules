#!/usr/bin/env python3
import math


def get_player_pos():
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            parts = raw.split(',')
            x, y, z = parts 
            float()
            return 
        except ValueError:
            print("Invalid syntax")


print("=== Game Coordinate System ===")
