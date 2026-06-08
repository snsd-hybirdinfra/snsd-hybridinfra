from pathlib import Path

ROOT = Path(".").resolve()

DELETE_NAME_PATTERNS = [
    "README.backup.md",
    "update_root_readme.ps1",
    "update_scenarios_readme.ps1",
]

DELETE_SUFFIXES = [
    ".bak",
    ".backup",
    ".tmp",
    ".broken",
]

DELETE_DIRECTORIES = [
    "runtime-workspace",
]

PROTECTED_PARTS = [
    "backup-automation-foundation",
    "backup-job-monitoring",
    "backup-failure-correlation",
    "backup-restoration-automation",
]

deleted = []
protected_skipped = 0

for dirname in DELETE_DIRECTORIES:
    target = ROOT / dirname
    if target.exists() and target.is_dir():
        for child in sorted(target.rglob("*"), reverse=True):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                child.rmdir()
        target.rmdir()
        deleted.append(dirname + "/")

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    rel = path.relative_to(ROOT).as_posix()

    should_delete = False

    if path.name in DELETE_NAME_PATTERNS:
        should_delete = True

    if any(path.name.endswith(suffix) for suffix in DELETE_SUFFIXES):
        should_delete = True

    if not should_delete:
        continue

    if any(protected in rel for protected in PROTECTED_PARTS):
        protected_skipped += 1
        continue

    path.unlink()
    deleted.append(rel)

print("[OK] cleanup completed")
print(f"deleted_files: {len(deleted)}")
print(f"protected_files_skipped: {protected_skipped}")

if deleted:
    print("")
    print("[DELETED]")
    for item in deleted:
        print(f"- {item}")

