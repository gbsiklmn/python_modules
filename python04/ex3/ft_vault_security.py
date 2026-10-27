#!/usr/bin/env python3

def secure_archive(filename: str, action: str = "read", content: str = None) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                content = f.read()
            return (True, content)
        elif action == "write":
            with open(filename, "w") as f:
                content2 = f.write()
        else:
            return (False, str(e))
    except OSError as e:
        return (False, str(e))

    except UnicodeDecodeError as e:
        return (False, str(e))


if __name__ == "__main__":
    print(secure_archive("/not/existing/file"))
    print(secure_archive("/etc/shadow"))
    print(secure_archive("/bin/ls"))
    print(secure_archive("ancient_fragment.txt"))
    print(secure_archive("new_fragment.txt", "write", "hello\n"))
