def whisper_cipher(text: str, shift: int) -> str:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for c in text:
        if c in lower:
            result += lower[(lower.find(c) + shift) % 26]
        elif c in upper:
            result += upper[(upper.find(c) + shift) % 26]
        else:
            result += c
    return result