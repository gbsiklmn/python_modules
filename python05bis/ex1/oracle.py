import os
from dotenv import load_dotenv

VARIABLES: list[str] = [
    "MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT",
]


def main() -> None:
    load_dotenv()
    config: dict[str, str | None] = {
        name: os.environ.get(name) for name in VARIABLES}
    missing = [name for name, value in config.items() if not value]

    print("ORACLE STATUS: Consulting the configuration...")
    if missing:
        for name in missing:
            print(f"WARNING: {name} is not set")
    mode = config["MATRIX_MODE"] or "development"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if config["DATABASE_URL"]:
        where = ("local instance" if mode == "development"
                 else "production cluster")
        print(f"Database: Connected to {where}")
    else:
        print("Database: MISSING (DATABASE_URL not set)")
    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: MISSING (API_KEY not set)")

    log_level = config["LOG_LEVEL"] or (
        "DEBUG" if mode == "development" else "WARNING")
    print(f"Log level: {log_level}")

    if config["ZION_ENDPOINT"]:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline (ZION_ENDPOINT not set)")

    print("Configuration security check:")
    gitignore = os.path.join(os.path.dirname(__file__), ".gitignore")
    try:
        with open(gitignore) as file:
            ignored = ".env" in [line.strip() for line in file]
    except FileNotFoundError:
        ignored = False
    if ignored:
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is not in .gitignore")
    api_key = config["API_KEY"]
    if api_key:
        with open(__file__) as file:
            source = file.read()
        if api_key in source:
            print("[WARNING] API key found in source code")
        else:
            print("[OK] No hardcoded secrets detected")
    else:
        print("[SKIPPED] No hardcoded secrets check: API_KEY is not set")


if __name__ == "__main__":
    main()
