#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError as e:
        raise ValueError(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("Input data is '25'")
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(e)
    print("Input data is 'abc'")
    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as e:
        print(e)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
