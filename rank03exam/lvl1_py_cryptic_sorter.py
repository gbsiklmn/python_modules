def sort_key(s: str) -> tuple:
    lowered = s.lower()
    vowels = 0
    for c in lowered:
        if c in "aeiou":
            vowels += 1
    return(len(s), lowered, vowels)

def cryptic_sorter(strings: list[str]) -> list[str]:
    result = list(strings)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if sort_key(result[j]) > sort_key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result