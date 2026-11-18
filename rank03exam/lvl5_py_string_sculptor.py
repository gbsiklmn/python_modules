def string_sculptor(text: str) -> str:
    result = ""
    index = 0
    for c in text:
        if c.isalpha():
            if index % 2 == 0:
                result += c.lower()
            else:
                result += c.upper()
            index += 1
        else:
            result += c
    return result