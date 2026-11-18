def anagram(s1: str, s2: str) -> bool:
    a = s1.lower().replace(" ", "")
    b = s2.lower().replace(" ", "")
    for c in a:
        if c not in b:
            return False
        b = b.replace(c, "", 1)
    return not b