from pathlib import Path

ROOT = Path(".").resolve()

DELETE_NAME_PATTERNS = [
    "a.txt",
    "README.backup.md",
    "update_root_readme.ps1",
    "remove_forced_flagship_concept.ps1",
    "update_scenarios_readme.ps1",
]

DELETE_SUFFIXES = [
    ".bak",
    ".backup",
    ".tmp",
    ".broken",
]

PROTECTED_PARTS = [
    "backup-automation-foundation",
    "backup-job-monitoring",
    "backup-failure-correlation",
    "backup-restoration-automation",
]

deleted = []
skipped = []

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    rel = path.relative_to(ROOT).as_posix()

    if any(protected in rel for protected in PROTECTED_PARTS):
        skipped.append(rel)
        continue

    should_delete = False

    if path.name in DELETE_NAME_PATTERNS:
        should_delete = True

    if any(path.name.endswith(suffix) for suffix in DELETE_SUFFIXES):
        should_delete = True

    if should_delete:
        path.unlink()
        deleted.append(rel)

print("[OK] cleanup completed")
print(f"deleted_files: {len(deleted)}")

for item in deleted:
    print(f"- {item}")

if skipped:
    print("")
    print("[INFO] protected paths skipped:")
    for item in skipped:
        print(f"- {item}")
