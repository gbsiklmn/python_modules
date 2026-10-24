#!/usr/bin/env python3
import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO[str] = open(filename, "r")

        print("---")
        content = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
        print("Transform data: ")
        print("---")
        

    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()