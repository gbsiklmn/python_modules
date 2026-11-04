import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if in_virtual_env():
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print("Reagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
