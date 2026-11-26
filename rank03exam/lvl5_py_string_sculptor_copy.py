def twist_sequence(arr: list[int], k: int) -> list[int]:
    swap = False
    r = ""
    for c in arr:
        if c.lower() in "abcedefghijklmnopqrstuvwxyz":
            if not swap:
                r = r + c.lower()
            else:
                r = r + c.upper()
            swap = not swap
        else:
            r = r + c