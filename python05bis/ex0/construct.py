import os
import site
import sys

def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix

def main() -> None:
    if in_virtual_env():
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment:{os.path.basename(sys.prefix)} ")
        print("SUCCESS: You are working in an isolated environment!")
    else:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment:{os.path.basename(sys.prefix)} ")


if __name__ == "__main__":
    main()