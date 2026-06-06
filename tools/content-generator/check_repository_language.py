from pathlib import Path
import sys

ROOT = Path(".").resolve()
REPORT = ROOT / "reports" / "repository-language-check.md"

SCAN_EXTENSIONS = {
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".py",
    ".ps1",
    ".txt",
}

EXCLUDED_DIR_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}

EXCLUDED_FILE_NAMES = {
    "repository-language-check.md",
}

EXCLUDED_PATH_PARTS = {
    # Generated evidence can contain legacy placeholder wording
    # without affecting reviewer-facing scenario README quality.
    "evidence/generated",

    # Legacy placeholder artifact generator is retained only as a utility reference.
    "generate_placeholder_artifacts.py",

    # This checker necessarily contains the blocked terms as pattern definitions.
    "check_repository_language.py",
}

BAD_PATTERNS = [
    "TODO",
    "TBD",
    "lorem",
    "example.com",
    "your-",
    "癤",
    "�",
    "占",
    "forced flagship",
    "flagship",
]

hits = []

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    rel = path.relative_to(ROOT).as_posix()

    if any(part in EXCLUDED_DIR_NAMES for part in path.parts):
        continue

    if path.name in EXCLUDED_FILE_NAMES:
        continue

    if any(excluded in rel for excluded in EXCLUDED_PATH_PARTS):
        continue

    if path.suffix.lower() not in SCAN_EXTENSIONS:
        continue

    text = path.read_text(encoding="utf-8-sig", errors="replace")

    for line_no, line in enumerate(text.splitlines(), start=1):
        lower_line = line.lower()

        for pattern in BAD_PATTERNS:
            if pattern.lower() in lower_line:
                hits.append((rel, line_no, pattern, line.strip()))

lines = []
lines.append("# Repository Language Check")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("```text")
lines.append(f"scanned_extensions: {', '.join(sorted(SCAN_EXTENSIONS))}")
lines.append(f"bad_patterns: {len(BAD_PATTERNS)}")
lines.append(f"bad_pattern_hits: {len(hits)}")
lines.append("```")
lines.append("")
lines.append("## Scan Scope")
lines.append("")
lines.append("```text")
lines.append("included: reviewer-facing markdown, metadata, scripts, reports, and repository documentation")
lines.append("excluded: generated evidence artifacts, checker self-pattern definitions, legacy placeholder artifact generator")
lines.append("```")
lines.append("")
lines.append("## Pattern Hits")
lines.append("")
lines.append("| File | Line | Pattern | Text |")
lines.append("|---|---:|---|---|")

if hits:
    for rel, line_no, pattern, line in hits:
        safe_line = line.replace("|", "\\|")
        lines.append(f"| `{rel}` | {line_no} | `{pattern}` | {safe_line} |")
else:
    lines.append("| NONE | 0 | NONE | NONE |")

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"[OK] wrote {REPORT}")
print(f"[OK] bad pattern hits: {len(hits)}")

if hits:
    sys.exit(1)
