#!/usr/bin/env python3

def secure_archive(filename: str, action: str = "read", content: str | None = None) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)
        elif action == "write":
            if content is None:
                return (False, "The content is missing")
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action: use 'read' or 'write'")
    except OSError as e:
        return (False, str(e))

    except UnicodeDecodeError as e:
        return (False, str(e))

def main():
    print("=== Cyber Archives Security ===")
    print(secure_archive("/not/existing/file"))
    print(secure_archive("/etc/shadow"))
    print(secure_archive("/bin/ls"))
    print(secure_archive("ancient_fragment.txt"))
    print(secure_archive("new_fragment.txt", "write", "hello\n"))
    print(secure_archive("anything", "delete"))
    print(secure_archive("new_fragment.txt", "write"))
    ok, text = secure_archive("ancient_fragment.txt")
    print(secure_archive("new_fragment.txt", "write", text))
    print(secure_archive("/etc/passwd", "write", "hello\n"))
    

if __name__ == "__main__":
    main()

