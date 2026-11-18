def twist_sequence(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    if n == 0:
        return []
    k = k % n
    return arr[n - k:] + arr[:n - k]