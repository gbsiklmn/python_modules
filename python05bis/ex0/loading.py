import importlib

REAGENTS: list[tuple[str, str]] = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
]


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    missing: list[str] = []
    for name, purpose in REAGENTS:
        try:
            module = importlib.import_module(name)
            print(f"[OK] {name} ({module.__version__}) - {purpose}")
        except ImportError:
            print(f"[MISSING] {name}")
            missing.append(name)

    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins the resolved")
    print("versions in poetry.lock so every install is identical.")
    if missing:
        names = " ".join(missing)
        print(f"Missing reagents: {names}")
        print(f"Install with pip: pip install {names}")
        print(f"Install with Poetry: poetry add {names}")

    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
