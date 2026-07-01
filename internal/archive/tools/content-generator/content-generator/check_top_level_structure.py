from pathlib import Path

ROOT = Path(".").resolve()
REPORT = ROOT / "reports" / "top-level-structure-check.md"

expected_dirs = [
    "scenarios",
    "modules",
    "adapters",
    "shared-runtime",
    "tools",
    "reports",
    "builds",
    "docs",
    "labs",
    "validation-reports",
    "diagrams",
    "internal",
]

actual_dirs = sorted([
    p.name for p in ROOT.iterdir()
    if p.is_dir() and not p.name.startswith(".")
])

missing_dirs = [name for name in expected_dirs if not (ROOT / name).is_dir()]
extra_dirs = [name for name in actual_dirs if name not in expected_dirs]

readme = ROOT / "README.md"
readme_text = readme.read_text(encoding="utf-8-sig", errors="replace") if readme.exists() else ""

missing_readme_mentions = [
    name for name in expected_dirs
    if name not in readme_text
]

lines = []
lines.append("# Top-Level Structure Check")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("```text")
lines.append(f"expected_directories: {len(expected_dirs)}")
lines.append(f"actual_top_level_directories: {len(actual_dirs)}")
lines.append(f"missing_expected_directories: {len(missing_dirs)}")
lines.append(f"extra_top_level_directories: {len(extra_dirs)}")
lines.append(f"missing_root_readme_mentions: {len(missing_readme_mentions)}")
lines.append("```")
lines.append("")
lines.append("## Expected Directories")
lines.append("")
lines.append("```text")
lines.extend(expected_dirs)
lines.append("```")
lines.append("")
lines.append("## Actual Top-Level Directories")
lines.append("")
lines.append("```text")
lines.extend(actual_dirs)
lines.append("```")
lines.append("")
lines.append("## Missing Expected Directories")
lines.append("")
lines.append("```text")
lines.extend(missing_dirs if missing_dirs else ["NONE"])
lines.append("```")
lines.append("")
lines.append("## Extra Top-Level Directories")
lines.append("")
lines.append("```text")
lines.extend(extra_dirs if extra_dirs else ["NONE"])
lines.append("```")
lines.append("")
lines.append("## Missing Root README Mentions")
lines.append("")
lines.append("```text")
lines.extend(missing_readme_mentions if missing_readme_mentions else ["NONE"])
lines.append("```")

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"[OK] wrote {REPORT}")
print(f"[OK] missing dirs: {len(missing_dirs)}")
print(f"[OK] extra dirs: {len(extra_dirs)}")
print(f"[OK] missing README mentions: {len(missing_readme_mentions)}")

