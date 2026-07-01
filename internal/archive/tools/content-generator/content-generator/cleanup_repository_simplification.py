from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]

REMOVE_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
    "runtime-workspace",
}

REMOVE_FILE_NAMES = {
    "tree.md",
}

REMOVE_FILE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".bak",
    ".tmp",
    ".temp",
    ".log",
}

PRESERVE_ROOT_FILE_NAMES = {
    "README.md",
    ".gitignore",
    ".gitattributes",
    "a.txt",
}

def should_remove_root_extra(path: Path) -> bool:
    if path.parent != ROOT:
        return False

    name = path.name

    if name in PRESERVE_ROOT_FILE_NAMES:
        return False

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
        print(f"[REMOVE] directory: {path.relative_to(ROOT)}")
    elif path.is_file():
        path.unlink(missing_ok=True)
        print(f"[REMOVE] file: {path.relative_to(ROOT)}")

def main() -> None:
    removed = 0

    for path in sorted(ROOT.rglob("*"), reverse=True):
        if ".git" in path.parts:
            continue

        if path.is_dir() and path.name in REMOVE_DIR_NAMES:
            remove_path(path)
            removed += 1
            continue

        if path.is_file() and path.name in REMOVE_FILE_NAMES:
            remove_path(path)
            removed += 1
            continue

        if path.is_file() and path.suffix in REMOVE_FILE_SUFFIXES:
            remove_path(path)
            removed += 1
            continue

    for path in ROOT.iterdir():
        if path.is_file() and should_remove_root_extra(path):
            remove_path(path)
            removed += 1

    print(f"[OK] simplification cleanup completed. removed={removed}")

if __name__ == "__main__":
    main()
