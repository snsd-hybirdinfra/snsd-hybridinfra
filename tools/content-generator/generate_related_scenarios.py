from pathlib import Path
from collections import defaultdict
import re
import yaml

ROOT = Path(".").resolve()
SCENARIOS_ROOT = ROOT / "scenarios"
REPORT_PATH = ROOT / "reports" / "related-scenarios-generation-report.md"
A_TXT = ROOT / "a.txt"

LEVEL_ORDER = [
    "level-1-visibility",
    "level-2-correlation",
    "level-3-recovery",
    "level-4-resilience",
    "level-5-continuity",
]

STOP_WORDS = {
    "monitoring", "visibility", "correlation", "analysis",
    "recovery", "automation", "orchestration", "resilience",
    "continuity", "failover", "service", "health", "runtime",
    "operational", "enterprise", "infrastructure", "coordination",
    "workflow", "scenario"
}

def repo_path(path: str) -> str:
    return "/snsd-hybridinfra/" + path.replace("\\", "/").strip("/")

def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

def dump_yaml(path: Path, data: dict):
    path.write_text(
        yaml.safe_dump(
            data,
            sort_keys=False,
            allow_unicode=True,
            width=1000,
        ),
        encoding="utf-8",
    )

def tokens(value: str) -> set[str]:
    return {
        item
        for item in re.split(r"[^a-zA-Z0-9]+", str(value).lower())
        if item and item not in STOP_WORDS
    }

def score(source: dict, candidate: dict) -> int:
    if source["domain"] != candidate["domain"]:
        return -1

    value = 100
    value += len(tokens(source["name"]) & tokens(candidate["name"])) * 20
    return value

def adjacent_level(level: str, offset: int):
    if level not in LEVEL_ORDER:
        return None

    index = LEVEL_ORDER.index(level) + offset

    if index < 0 or index >= len(LEVEL_ORDER):
        return None

    return LEVEL_ORDER[index]

def pick_exact_domain(source: dict, candidates: list[dict], limit: int) -> list[str]:
    ranked = sorted(
        [
            (score(source, candidate), candidate)
            for candidate in candidates
            if candidate["path"] != source["path"]
            and candidate["domain"] == source["domain"]
        ],
        key=lambda item: (-item[0], item[1]["name"]),
    )

    selected = []

    for value, candidate in ranked:
        if value < 0:
            continue

        selected.append(repo_path(candidate["path"]))

        if len(selected) >= limit:
            break

    return selected

rows = []
by_level = defaultdict(list)

for metadata_path in sorted(SCENARIOS_ROOT.glob("*/*/metadata.yaml")):
    data = load_yaml(metadata_path)
    scenario_dir = metadata_path.parent
    rel_path = str(scenario_dir.relative_to(ROOT)).replace("\\", "/")

    row = {
        "name": data.get("scenario_name", scenario_dir.name),
        "title": data.get("scenario_title", scenario_dir.name),
        "level": data.get("lifecycle_level", scenario_dir.parent.name),
        "domain": data.get("primary_domain", "Unknown"),
        "path": rel_path,
        "metadata_path": metadata_path,
        "data": data,
    }

    rows.append(row)
    by_level[row["level"]].append(row)

for row in rows:
    upstream_level = adjacent_level(row["level"], -1)
    downstream_level = adjacent_level(row["level"], 1)

    same_level = pick_exact_domain(
        row,
        by_level.get(row["level"], []),
        3,
    )

    upstream = []
    if upstream_level:
        upstream = pick_exact_domain(
            row,
            by_level.get(upstream_level, []),
            1,
        )

    downstream = []
    if downstream_level:
        downstream = pick_exact_domain(
            row,
            by_level.get(downstream_level, []),
            1,
        )

    row["data"]["related_scenarios"] = {
        "upstream": upstream,
        "same_level": same_level,
        "downstream": downstream,
        "cross_domain": [],
    }

for row in rows:
    dump_yaml(row["metadata_path"], row["data"])

report_rows = []

for metadata_path in sorted(SCENARIOS_ROOT.glob("*/*/metadata.yaml")):
    data = load_yaml(metadata_path)
    related = data.get("related_scenarios", {}) or {}

    counts = {
        "upstream": len(related.get("upstream", [])),
        "same_level": len(related.get("same_level", [])),
        "downstream": len(related.get("downstream", [])),
        "cross_domain": len(related.get("cross_domain", [])),
    }

    report_rows.append({
        "name": data.get("scenario_name", metadata_path.parent.name),
        "level": data.get("lifecycle_level", metadata_path.parent.parent.name),
        "domain": data.get("primary_domain", "Unknown"),
        "path": str(metadata_path.parent.relative_to(ROOT)).replace("\\", "/"),
        "related": related,
        "total": sum(counts.values()),
        **counts,
    })

empty = [row for row in report_rows if row["total"] == 0]

lines = []
lines.append("# Strict Related Scenarios Generation Report")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("```text")
lines.append(f"total_scenarios: {len(report_rows)}")
lines.append(f"empty_related_scenarios: {len(empty)}")
lines.append("rule: exact primary_domain only; no fallback; no forced representative chain")
lines.append("```")
lines.append("")
lines.append("## Empty Related Scenarios")
lines.append("")
lines.append("```text")
if empty:
    for row in empty:
        lines.append(f"{row['level']} | {row['domain']} | {row['name']}")
else:
    lines.append("NONE")
lines.append("```")
lines.append("")
lines.append("## Relationship Counts")
lines.append("")
lines.append("```text")
for row in report_rows:
    lines.append(
        f"{row['level']} | {row['name']} | "
        f"up={row['upstream']} same={row['same_level']} "
        f"down={row['downstream']} cross={row['cross_domain']}"
    )
lines.append("```")
lines.append("")
lines.append("## Quality Guard Samples")
lines.append("")
sample_names = [
    "api-gateway-health-monitoring",
    "certificate-expiration-monitoring",
    "vpn-connectivity-monitoring",
    "vpn-latency-correlation",
    "vpn-tunnel-recovery-automation",
    "multi-site-routing-failover",
    "enterprise-operational-continuity",
    "database-health-monitoring",
    "security-event-monitoring",
    "network-path-visibility",
]

for name in sample_names:
    row = next((item for item in report_rows if item["name"] == name), None)

    if not row:
        continue

    lines.append(f"### {row['name']}")
    lines.append("```yaml")
    lines.append(f"domain: {row['domain']}")
    lines.append("related_scenarios:")
    for key in ["upstream", "same_level", "downstream", "cross_domain"]:
        lines.append(f"  {key}: {row['related'].get(key, [])}")
    lines.append("```")
    lines.append("")

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
A_TXT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

print(f"[OK] updated metadata files: {len(report_rows)}")
print(f"[OK] empty related scenarios: {len(empty)}")
print(f"[OK] report: {REPORT_PATH}")
print(f"[OK] a.txt: {A_TXT}")

