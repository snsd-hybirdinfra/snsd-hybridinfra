from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT_PATH = ROOT / "reports" / "repository-simplification-candidates.md"

CORE_TOP_LEVEL = {
    ".git",
    "README.md",
    ".gitignore",
    ".gitattributes",
    "adapters",
    "builds",
    "diagrams",
    "docs",
    "internal",
    "labs",
    "modules",
    "reports",
    "scenarios",
    "shared-runtime",
    "tools",
    "validation-reports",
}

ALWAYS_IGNORE = {
    ".git",
}

DELETE_CANDIDATE_NAMES = {
    "__pycache__",
    ".pytest_cache",
    "runtime-workspace",
    "tree.md",
}

DELETE_CANDIDATE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".bak",
    ".tmp",
    ".temp",
    ".log",
}

LOCAL_ONLY_KEEP = {
    "a.txt",
}

def is_accidental_root_file(path: Path) -> bool:
    if path.parent != ROOT:
        return False

    name = path.name

    if name in CORE_TOP_LEVEL:
        return False

    if name in LOCAL_ONLY_KEEP:
        return False

    if name.startswith("lab is"):
        return True

    if name.startswith("validated"):
        return True

    if "\uf07c" in name:
        return True

    return False

def main() -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    cache_dirs = []
    generated_junk = []
    root_extras = []
    backup_files = []
    local_only = []

    for path in ROOT.rglob("*"):
        if any(part in ALWAYS_IGNORE for part in path.parts):
            continue

        rel = path.relative_to(ROOT)

        if path.is_dir() and path.name in DELETE_CANDIDATE_NAMES:
            cache_dirs.append(rel.as_posix())
            continue

        if path.is_file() and path.suffix in DELETE_CANDIDATE_SUFFIXES:
            if path.suffix == ".bak":
                backup_files.append(rel.as_posix())
            else:
                generated_junk.append(rel.as_posix())
            continue

    for path in ROOT.iterdir():
        if path.name in ALWAYS_IGNORE:
            continue

        if path.name in LOCAL_ONLY_KEEP:
            local_only.append(path.name)
            continue

        if path.name not in CORE_TOP_LEVEL:
            root_extras.append(path.name)

        if is_accidental_root_file(path):
            generated_junk.append(path.name)

    lines = []
    lines.append("# Repository Simplification Candidates")
    lines.append("")
    lines.append("This report lists files and directories that may be removed or reviewed before implementation work begins.")
    lines.append("")
    lines.append("## Policy")
    lines.append("")
    lines.append("- Core repository directories are preserved.")
    lines.append("- Local-only executive summary file a.txt is preserved.")
    lines.append("- Cache, temporary, backup, accidental root files, and runtime outputs are removal candidates.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Cache/runtime directories: {len(cache_dirs)}")
    lines.append(f"- Generated junk files: {len(generated_junk)}")
    lines.append(f"- Backup files: {len(backup_files)}")
    lines.append(f"- Root-level extra items: {len(root_extras)}")
    lines.append(f"- Local-only preserved files: {len(local_only)}")
    lines.append("")

    sections = [
        ("Cache and Runtime Directories", cache_dirs),
        ("Generated Junk Files", generated_junk),
        ("Backup Files", backup_files),
        ("Root-Level Extra Items", root_extras),
        ("Local-Only Preserved Files", local_only),
    ]

    for title, items in sections:
        lines.append(f"## {title}")
        lines.append("")
        if items:
            for item in sorted(set(items)):
                lines.append(f"- {item}")
        else:
            lines.append("- None")
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] wrote {REPORT_PATH.relative_to(ROOT)}")
    print(f"[OK] cache/runtime directories: {len(cache_dirs)}")
    print(f"[OK] generated junk files: {len(generated_junk)}")
    print(f"[OK] backup files: {len(backup_files)}")
    print(f"[OK] root-level extra items: {len(root_extras)}")
    print(f"[OK] local-only preserved files: {len(local_only)}")

if __name__ == "__main__":
    main()
