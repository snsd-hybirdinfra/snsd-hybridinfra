from pathlib import Path
from collections import defaultdict
import yaml

ROOT = Path(".").resolve()
SCENARIOS_ROOT = ROOT / "scenarios"
OUT = SCENARIOS_ROOT / "README.md"

LEVEL_LABELS = {
    "level-1-visibility": "Level 1 - Visibility",
    "level-2-correlation": "Level 2 - Correlation",
    "level-3-recovery": "Level 3 - Recovery",
    "level-4-resilience": "Level 4 - Resilience",
    "level-5-continuity": "Level 5 - Continuity",
}

LEVEL_PURPOSE = {
    "level-1-visibility": "Signal collection, health visibility, and operational state exposure.",
    "level-2-correlation": "Dependency analysis, symptom correlation, and impact reasoning.",
    "level-3-recovery": "Controlled recovery execution, automation workflow, and restoration validation.",
    "level-4-resilience": "Distributed failure-domain coordination and survivability validation.",
    "level-5-continuity": "Enterprise continuity governance, readiness validation, and operational reporting.",
}

LEVEL_ORDER = list(LEVEL_LABELS.keys())

def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

def clean(value):
    return str(value or "").replace("|", "\\|").strip()

rows = []

for metadata_path in sorted(SCENARIOS_ROOT.glob("*/*/metadata.yaml")):
    scenario_dir = metadata_path.parent
    data = load_yaml(metadata_path)

    rel_path = scenario_dir.relative_to(ROOT).as_posix()
    readme_path = f"./{scenario_dir.relative_to(SCENARIOS_ROOT).as_posix()}/README.md"

    related = data.get("related_scenarios", {}) or {}
    related_count = sum(len(related.get(key, []) or []) for key in ["upstream", "same_level", "downstream", "cross_domain"])

    rows.append({
        "level": data.get("lifecycle_level", scenario_dir.parent.name),
        "name": data.get("scenario_name", scenario_dir.name),
        "title": data.get("scenario_title", scenario_dir.name.replace("-", " ").title()),
        "domain": data.get("primary_domain", "Unknown"),
        "status": data.get("status", "draft"),
        "path": rel_path,
        "readme": readme_path,
        "related_count": related_count,
    })

by_level = defaultdict(list)
by_domain = defaultdict(int)

for row in rows:
    by_level[row["level"]].append(row)
    by_domain[row["domain"]] += 1

lines = []
lines.append("# Scenario Inventory")
lines.append("")
lines.append("This directory contains lifecycle-aligned infrastructure operations scenarios for the SNSD Hybrid Infrastructure portfolio.")
lines.append("")
lines.append("The scenario set is designed to demonstrate operational breadth across visibility, correlation, recovery, resilience, and continuity workflows. Scenarios are organized by lifecycle maturity level rather than by a single representative incident chain.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Inventory Summary")
lines.append("")
lines.append(f"- Total scenarios: {len(rows)}")
for level in LEVEL_ORDER:
    lines.append(f"- {LEVEL_LABELS[level]}: {len(by_level.get(level, []))}")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Lifecycle Coverage")
lines.append("")
lines.append("| Level | Scenario Count | Operational Focus |")
lines.append("|---|---:|---|")
for level in LEVEL_ORDER:
    lines.append(f"| {LEVEL_LABELS[level]} | {len(by_level.get(level, []))} | {LEVEL_PURPOSE[level]} |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Domain Coverage")
lines.append("")
lines.append("| Domain | Scenario Count |")
lines.append("|---|---:|")
for domain, count in sorted(by_domain.items(), key=lambda item: (-item[1], item[0])):
    lines.append(f"| {clean(domain)} | {count} |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Scenario Index")
lines.append("")

for level in LEVEL_ORDER:
    items = sorted(by_level.get(level, []), key=lambda item: item["name"])
    lines.append(f"### {LEVEL_LABELS[level]}")
    lines.append("")
    lines.append(LEVEL_PURPOSE[level])
    lines.append("")
    lines.append("| Scenario | Domain | Status | Related Links |")
    lines.append("|---|---|---|---:|")

    for item in items:
        lines.append(
            f"| [{clean(item['title'])}]({item['readme']}) | "
            f"{clean(item['domain'])} | "
            f"{clean(item['status'])} | "
            f"{item['related_count']} |"
        )

    lines.append("")

lines.append("---")
lines.append("")
lines.append("## Scenario Artifact Standard")
lines.append("")
lines.append("Each scenario is expected to include the following reviewer-readable artifacts:")
lines.append("")
lines.append("    metadata.yaml")
lines.append("    README.md")
lines.append("    diagrams/operational-poster.svg")
lines.append("    diagrams/operational-poster.png")
lines.append("    evidence/generated/summary.md")
lines.append("    evidence/generated/execution-evidence.md")
lines.append("    evidence/generated/validation-evidence.md")
lines.append("    evidence/generated/artifact-manifest.json")
lines.append("    evidence/generated/artifact-checksums.json")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Validation Reports")
lines.append("")
lines.append("- [Repository Quality Check](../reports/repository-quality-check.md)")
lines.append("- [Related Scenarios Generation Report](../reports/related-scenarios-generation-report.md)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("The scenario inventory provides lifecycle-based operational coverage across infrastructure domains. It supports portfolio review by showing scenario distribution, operational focus, domain coverage, and artifact consistency from one index page.")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"[OK] wrote {OUT}")
print(f"[OK] total scenarios: {len(rows)}")
