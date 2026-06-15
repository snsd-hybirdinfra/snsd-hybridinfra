from pathlib import Path
import csv
from collections import defaultdict

INPUT = Path("reports/scenario-required-data-map.csv")
OUTPUT = Path("scenarios/README.md")

LEVEL_TITLES = {
    "level-1-visibility": "Level 1 - Visibility",
    "level-2-correlation": "Level 2 - Correlation",
    "level-3-recovery": "Level 3 - Recovery",
    "level-4-resilience": "Level 4 - Resilience",
    "level-5-continuity": "Level 5 - Continuity",
}

def md_link(title: str, path: str) -> str:
    rel = path.replace("\\", "/").replace("scenarios/", "")
    return f"[{title}]({rel}/)"

with INPUT.open("r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

by_level = defaultdict(list)
for row in rows:
    by_level[row["lifecycle_level"]].append(row)

lines = []
lines.append("# Operational Scenarios")
lines.append("")
lines.append("This directory contains lifecycle-based infrastructure operations scenarios.")
lines.append("")
lines.append("Scenarios are organized by operational maturity level, from visibility and detection through correlation, recovery, resilience, and continuity governance.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Scenario Lifecycle")
lines.append("")
lines.append("| Level | Purpose |")
lines.append("|---|---|")
lines.append("| Level 1 - Visibility | Monitoring, telemetry, health visibility, and detection evidence |")
lines.append("| Level 2 - Correlation | Dependency analysis, signal correlation, and impact reasoning |")
lines.append("| Level 3 - Recovery | Recovery workflow, automation, restoration, and validation |")
lines.append("| Level 4 - Resilience | Distributed failover, survivability, and multi-site resilience |")
lines.append("| Level 5 - Continuity | Enterprise continuity, governance, and executive reporting |")
lines.append("")
lines.append("---")
lines.append("")

for level in sorted(by_level.keys()):
    title = LEVEL_TITLES.get(level, level)
    items = sorted(by_level[level], key=lambda x: x["scenario_name"])

    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"Scenario count: **{len(items)}**")
    lines.append("")
    lines.append("| Scenario | Domain | Type | Target Resource |")
    lines.append("|---|---|---|---|")

    for row in items:
        scenario = md_link(row["scenario_title"], row["scenario_path"])
        domain = row["primary_domain"]
        scenario_type = row["scenario_type"]
        target = row["target_resource"]
        lines.append(f"| {scenario} | {domain} | {scenario_type} | {target} |")

    lines.append("")
    lines.append("---")
    lines.append("")

lines.append("## Summary")
lines.append("")
lines.append("This scenario catalog provides a reviewer-readable index of the operational scenarios in the portfolio.")
lines.append("")
lines.append("Each scenario README documents scenario metadata, operational context, used modules, infrastructure components, lifecycle workflow, validation criteria, and evidence references.")
lines.append("")

OUTPUT.write_text("\n".join(lines), encoding="utf-8")
print(f"[OK] generated {OUTPUT}")
print(f"[OK] scenario count: {len(rows)}")
