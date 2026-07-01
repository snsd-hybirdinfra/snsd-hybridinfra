from pathlib import Path
import re

ROOT = Path(".").resolve()
REPORT = ROOT / "reports" / "markdown-link-check.md"

readme_files = sorted(ROOT.rglob("README.md"))

link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

broken = []
checked = []

for readme in readme_files:
    text = readme.read_text(encoding="utf-8-sig", errors="replace")
    base = readme.parent

    for match in link_pattern.finditer(text):
        link = match.group(1).strip()

        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue

        if link.startswith("/"):
            continue

        clean_link = link.split("#")[0]

        if not clean_link:
            continue

        target = (base / clean_link).resolve()
        checked.append((readme, link, target))

        if not target.exists():
            broken.append((readme, link, target))

lines = []
lines.append("# Markdown Link Check")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("```text")
lines.append(f"readme_files: {len(readme_files)}")
lines.append(f"checked_relative_links: {len(checked)}")
lines.append(f"broken_links: {len(broken)}")
lines.append("```")
lines.append("")
lines.append("## Broken Links")
lines.append("")
lines.append("```text")

if broken:
    for readme, link, target in broken:
        lines.append(f"{readme.relative_to(ROOT).as_posix()} -> {link}")
else:
    lines.append("NONE")

lines.append("```")

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"[OK] wrote {REPORT}")
print(f"[OK] readme files: {len(readme_files)}")
print(f"[OK] checked links: {len(checked)}")
print(f"[OK] broken links: {len(broken)}")
