from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]

REMOVE_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
}

REMOVE_FILE_SUFFIXES = {
    ".pyc",
    ".pyo",
}

REMOVE_ROOT_FILE_NAMES = {
    "tree.md",
}

PRESERVE_ROOT_FILE_NAMES = {
    "README.md",
    ".gitignore",
    ".gitattributes",
    "a.txt",
}

def is_accidental_root_file(path: Path) -> bool:
    name = path.name

    if path.parent != ROOT:
        return False

    if name in PRESERVE_ROOT_FILE_NAMES:
        return False

    if name in REMOVE_ROOT_FILE_NAMES:
        return True

    if name.startswith("lab is"):
        return True

    if name.startswith("validated"):
        return True

    if "\uf07c" in name:
        return True

    return False

def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path, ignore_errors=True)
        print(f"[CLEANUP] removed directory: {path.relative_to(ROOT)}")
    elif path.is_file():
        path.unlink(missing_ok=True)
        print(f"[CLEANUP] removed file: {path.relative_to(ROOT)}")

def main() -> None:
    removed = 0

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue

        if path.is_dir() and path.name in REMOVE_DIR_NAMES:
            remove_path(path)
            removed += 1
            continue

        if path.is_file() and path.suffix in REMOVE_FILE_SUFFIXES:
            remove_path(path)
            removed += 1
            continue

    for path in ROOT.iterdir():
        if path.is_file() and is_accidental_root_file(path):
            remove_path(path)
            removed += 1

    print(f"[CLEANUP] completed. removed={removed}")

if __name__ == "__main__":
    main()
