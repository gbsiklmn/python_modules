def string_permutation_checker(s1: str, s2: str) -> bool:
    b = s2
    for c in s1:
        if c not in b:
            return False
        b = b.replace(c, "", 1)
    return not b