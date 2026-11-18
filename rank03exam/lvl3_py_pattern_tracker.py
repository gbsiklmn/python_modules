def pattern_tracker(text: str) -> int:
    count = 0
    prev = ""
    for c in text:
        if prev and prev + c in "0123456789":
            count += 1
        prev = c
    return count