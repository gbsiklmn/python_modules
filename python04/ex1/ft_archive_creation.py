#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")

        print("---")
        content = file.read()
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
        print("Transform data:")
        print("---")
        lines = content.splitlines()
        new_lines = []
        for line in lines:
            new_lines.append(line + "#")

        new_content = "\n".join(new_lines) + "\n"
        print(new_content, end="")
        print("---")
        answer = input("Enter new file name (or empty): ")
        if answer == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{answer}'")
            f = open(answer, "w")
            f.write(new_content)
            f.close()
            print(f"Data saved in file '{answer}'.")

    except OSError as e:
        print(f"Error opening file '{e.filename}': {e}")
    except (KeyboardInterrupt, EOFError) as e:
        print("Error")


if __name__ == "__main__":
    main()
