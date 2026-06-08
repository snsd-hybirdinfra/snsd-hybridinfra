from pathlib import Path
import re

ROOT = Path(".").resolve()
README = ROOT / "README.md"
QUALITY = ROOT / "reports" / "repository-quality-check.md"

LEVELS = [
    ("level-1-visibility", "Level 1 Visibility scenarios"),
    ("level-2-correlation", "Level 2 Correlation scenarios"),
    ("level-3-recovery", "Level 3 Recovery scenarios"),
    ("level-4-resilience", "Level 4 Resilience scenarios"),
    ("level-5-continuity", "Level 5 Continuity scenarios"),
]

def count_level(level_dir: str) -> int:
    base = ROOT / "scenarios" / level_dir
    if not base.exists():
        return 0
    return len([p for p in base.iterdir() if p.is_dir()])

def read_quality_value(text: str, key: str) -> str:
    match = re.search(rf"{re.escape(key)}:\s*(.+)", text)
    return match.group(1).strip() if match else "UNKNOWN"

readme_text = README.read_text(encoding="utf-8-sig", errors="replace")
quality_text = QUALITY.read_text(encoding="utf-8-sig", errors="replace") if QUALITY.exists() else ""

counts = [(label, count_level(level_dir)) for level_dir, label in LEVELS]
total = sum(count for _, count in counts)

inventory_block = []
inventory_block.append("The repository currently contains:")
inventory_block.append("")
inventory_block.append(f"    Total scenarios: {total}")
for label, count in counts:
    inventory_block.append(f"    {label}: {count}")

inventory_pattern = (
    r"The repository currently contains:\s*\n\s*\n"
    r"    Total scenarios: \d+\s*\n"
    r"    Level 1 Visibility scenarios: \d+\s*\n"
    r"    Level 2 Correlation scenarios: \d+\s*\n"
    r"    Level 3 Recovery scenarios: \d+\s*\n"
    r"    Level 4 Resilience scenarios: \d+\s*\n"
    r"    Level 5 Continuity scenarios: \d+"
)

readme_text, inventory_changed = re.subn(
    inventory_pattern,
    "\n".join(inventory_block),
    readme_text,
    count=1,
)

quality_values = {
    "scenario_directories": read_quality_value(quality_text, "scenario_directories"),
    "metadata_files": read_quality_value(quality_text, "metadata_files"),
    "poster_svg_files": read_quality_value(quality_text, "poster_svg_files"),
    "poster_png_files": read_quality_value(quality_text, "poster_png_files"),
    "missing_required_artifacts": read_quality_value(quality_text, "missing_required_artifacts"),
    "small_png_files": read_quality_value(quality_text, "small_png_files"),
    "bad_phrase_hits": read_quality_value(quality_text, "bad_phrase_hits"),
    "readmes_with_empty_related_notice": read_quality_value(quality_text, "readmes_with_empty_related_notice"),
}

quality_block = []
quality_block.append("Current validation status:")
quality_block.append("")
for key, value in quality_values.items():
    quality_block.append(f"    {key}: {value}")

quality_pattern = (
    r"Current validation status:\s*\n\s*\n"
    r"    scenario_directories: .+\s*\n"
    r"    metadata_files: .+\s*\n"
    r"    poster_svg_files: .+\s*\n"
    r"    poster_png_files: .+\s*\n"
    r"    missing_required_artifacts: .+\s*\n"
    r"    small_png_files: .+\s*\n"
    r"    bad_phrase_hits: .+\s*\n"
    r"    readmes_with_empty_related_notice: .+"
)

readme_text, quality_changed = re.subn(
    quality_pattern,
    "\n".join(quality_block),
    readme_text,
    count=1,
)

if inventory_changed == 0:
    raise SystemExit("[FAIL] README scenario inventory block not found")

if quality_changed == 0:
    raise SystemExit("[FAIL] README quality status block not found")

README.write_text(readme_text, encoding="utf-8")

print("[OK] updated README inventory and quality status")
print(f"[OK] total scenarios: {total}")
for label, count in counts:
    print(f"[OK] {label}: {count}")
