def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    if number == "":
        return "ERROR"

    value = 0
    for c in number.upper():
        pos = digits.find(c)
        if pos == -1 or pos >= from_base:
            return "ERROR"
        value = value * from_base + pos

    if value == 0:
        return "0"

    result = ""
    while value > 0:
        result = digits[value % to_base] + result
        value = value // to_base
    return result