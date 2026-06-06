from pathlib import Path

ROOT = Path(".").resolve()
SCENARIOS = ROOT / "scenarios"
REPORT = ROOT / "reports" / "repository-quality-check.md"

required_files = [
    "README.md",
    "metadata.yaml",
    "diagrams/operational-poster.svg",
    "diagrams/operational-poster.png",
    "evidence/generated/summary.md",
    "evidence/generated/execution-evidence.md",
    "evidence/generated/validation-evidence.md",
    "evidence/generated/artifact-manifest.json",
    "evidence/generated/artifact-checksums.json",
]

bad_phrases = [
    "Detect operational condition",
    "Analyze infrastructure impact",
    "Execute response workflow",
    "Validate operational state",
    "operational condition represented by",
]

scenario_dirs = sorted([
    p for p in SCENARIOS.glob("*/*")
    if p.is_dir()
])

missing = []
small_png = []
bad_phrase_hits = []
empty_related_readme = []

for scenario in scenario_dirs:
    for rel in required_files:
        target = scenario / rel
        if not target.exists():
            missing.append(f"{scenario.as_posix()}/{rel}")

    png = scenario / "diagrams" / "operational-poster.png"
    if png.exists() and png.stat().st_size < 100000:
        small_png.append(f"{png.as_posix()} | {png.stat().st_size} bytes")

    for rel in ["README.md", "metadata.yaml", "diagrams/operational-poster.svg"]:
        target = scenario / rel
        if not target.exists():
            continue

        text = target.read_text(encoding="utf-8", errors="replace")
        for phrase in bad_phrases:
            if phrase in text:
                bad_phrase_hits.append(f"{target.as_posix()} | {phrase}")

    readme = scenario / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8", errors="replace")
        if "Related Scenarios" in text and "No related scenarios defined" in text:
            empty_related_readme.append(str(readme.relative_to(ROOT)).replace("\\", "/"))

lines = []
lines.append("# Repository Quality Check")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("```text")
lines.append(f"scenario_directories: {len(scenario_dirs)}")
lines.append(f"metadata_files: {len(list(SCENARIOS.rglob('metadata.yaml')))}")
lines.append(f"poster_svg_files: {len(list(SCENARIOS.rglob('operational-poster.svg')))}")
lines.append(f"poster_png_files: {len(list(SCENARIOS.rglob('operational-poster.png')))}")
lines.append(f"missing_required_artifacts: {len(missing)}")
lines.append(f"small_png_files: {len(small_png)}")
lines.append(f"bad_phrase_hits: {len(bad_phrase_hits)}")
lines.append(f"readmes_with_empty_related_notice: {len(empty_related_readme)}")
lines.append("```")
lines.append("")
lines.append("## Missing Required Artifacts")
lines.append("")
lines.append("```text")
lines.extend(missing if missing else ["NONE"])
lines.append("```")
lines.append("")
lines.append("## Small PNG Files")
lines.append("")
lines.append("```text")
lines.extend(small_png if small_png else ["NONE"])
lines.append("```")
lines.append("")
lines.append("## Bad Phrase Hits")
lines.append("")
lines.append("```text")
lines.extend(bad_phrase_hits if bad_phrase_hits else ["NONE"])
lines.append("```")
lines.append("")
lines.append("## README Empty Related Notices")
lines.append("")
lines.append("```text")
lines.extend(empty_related_readme if empty_related_readme else ["NONE"])
lines.append("```")

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"[OK] wrote {REPORT}")
