from pathlib import Path
import re
from datetime import datetime

ROOT = Path(".").resolve()
OUTPUT = ROOT / "a.txt"

def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        return ""
    return target.read_text(encoding="utf-8-sig", errors="replace")

def extract_value(text: str, key: str) -> str:
    match = re.search(rf"{re.escape(key)}:\s*(.+)", text)
    return match.group(1).strip() if match else "UNKNOWN"

def count_level(level_name: str) -> int:
    base = ROOT / "scenarios" / level_name
    if not base.exists():
        return 0
    return len([p for p in base.iterdir() if p.is_dir()])

quality = read("reports/repository-quality-check.md")
links = read("reports/markdown-link-check.md")
structure = read("reports/top-level-structure-check.md")
root_readme = read("reports/root-readme-alignment-check.md")
language = read("reports/repository-language-check.md")
related = read("reports/related-scenarios-generation-report.md")

levels = [
    ("level-1-visibility", "Level 1 Visibility"),
    ("level-2-correlation", "Level 2 Correlation"),
    ("level-3-recovery", "Level 3 Recovery"),
    ("level-4-resilience", "Level 4 Resilience"),
    ("level-5-continuity", "Level 5 Continuity"),
]

level_counts = [(label, count_level(level_dir)) for level_dir, label in levels]
total_scenarios = sum(count for _, count in level_counts)

lines = []
lines.append("SNSD HYBRID INFRASTRUCTURE - REPOSITORY SUMMARY REPORT")
lines.append("=" * 72)
lines.append("")
lines.append(f"Generated At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
lines.append("")
lines.append("1. Repository Positioning")
lines.append("-" * 72)
lines.append("SNSD Hybrid Infrastructure is an Enterprise Operational Capability Platform.")
lines.append("It organizes infrastructure operations as reusable capability modules, adapters,")
lines.append("shared runtime components, scenario workflows, generated artifacts, and validation reports.")
lines.append("")
lines.append("2. Scenario Inventory")
lines.append("-" * 72)
lines.append(f"Total Scenarios: {total_scenarios}")
for label, count in level_counts:
    lines.append(f"{label}: {count}")
lines.append("")
lines.append("3. Artifact Coverage")
lines.append("-" * 72)
lines.append(f"Scenario Directories: {extract_value(quality, 'scenario_directories')}")
lines.append(f"Metadata Files: {extract_value(quality, 'metadata_files')}")
lines.append(f"Poster SVG Files: {extract_value(quality, 'poster_svg_files')}")
lines.append(f"Poster PNG Files: {extract_value(quality, 'poster_png_files')}")
lines.append(f"Missing Required Artifacts: {extract_value(quality, 'missing_required_artifacts')}")
lines.append(f"Small PNG Files: {extract_value(quality, 'small_png_files')}")
lines.append("")
lines.append("4. Validation Status")
lines.append("-" * 72)
lines.append(f"Markdown Broken Links: {extract_value(links, 'broken_links')}")
lines.append(f"Top-Level Extra Directories: {extract_value(structure, 'extra_top_level_directories')}")
lines.append(f"Top-Level Missing Directories: {extract_value(structure, 'missing_expected_directories')}")
lines.append(f"Root README Missing Links: {extract_value(root_readme, 'missing_required_links')}")
lines.append(f"Root README Missing Terms: {extract_value(root_readme, 'missing_required_terms')}")
lines.append(f"Repository Language Hits: {extract_value(language, 'bad_pattern_hits')}")
lines.append("Related Mapping Policy: Conservative lifecycle-only mapping")
lines.append(f"Related Mapping Pending: {extract_value(related, 'empty_related_scenarios')}")
lines.append("")
lines.append("5. Platform Layers")
lines.append("-" * 72)
lines.append("scenarios/: lifecycle-based operational scenario workflows")
lines.append("modules/: reusable operational capability modules")
lines.append("adapters/: tool and platform integration adapters")
lines.append("shared-runtime/: shared orchestration, telemetry, evidence, and integration runtime")
lines.append("tools/: content generation, validation, and diagram rendering tooling")
lines.append("reports/: generated repository quality and health reports")
lines.append("builds/: build foundation documentation")
lines.append("docs/: repository documentation")
lines.append("")
lines.append("6. Current Baseline")
lines.append("-" * 72)

status_checks = [
    extract_value(quality, "missing_required_artifacts") == "0",
    extract_value(quality, "small_png_files") == "0",
    extract_value(links, "broken_links") == "0",
    extract_value(structure, "extra_top_level_directories") == "0",
    extract_value(structure, "missing_expected_directories") == "0",
    extract_value(root_readme, "missing_required_links") == "0",
    extract_value(root_readme, "missing_required_terms") == "0",
    extract_value(language, "bad_pattern_hits") == "0",
]

baseline_status = "PASS" if all(status_checks) else "CHECK_REQUIRED"

lines.append(f"Portfolio Baseline Status: {baseline_status}")
lines.append("Validation Workflow: tools/content-generator/run_repository_validation.py")
lines.append("")
lines.append("7. Operational Summary")
lines.append("-" * 72)
lines.append("The repository is structured as a production-oriented infrastructure operations")
lines.append("portfolio with lifecycle-based scenarios, reusable modules, generated evidence,")
lines.append("visual operational posters, index documentation, and repeatable validation tooling.")
lines.append("")
lines.append("=" * 72)
lines.append("END OF REPORT")
lines.append("")

OUTPUT.write_text("\n".join(lines), encoding="utf-8")

print(f"[OK] wrote {OUTPUT}")
print(f"[OK] portfolio baseline status: {baseline_status}")
print(f"[OK] total scenarios: {total_scenarios}")


