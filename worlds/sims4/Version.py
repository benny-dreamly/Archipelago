VERSION: tuple[int, int, int] | tuple[int, int, int, str] = (2, 0, 0, "rc2")

def version_to_str(version: tuple[int, int, int] | tuple[int, int, int, str]) -> str:
    if len(version) == 3:
        return f"{version[0]}.{version[1]}.{version[2]}"
    else:
        major, minor, patch, suffix = version
        return f"{major}.{minor}.{patch}-{suffix}"