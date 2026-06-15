from pathlib import Path

MODULE_ROOT = Path("modules")
OUTPUT = MODULE_ROOT / "README.md"

MODULE_DESCRIPTIONS = {
    "infrastructure-provisioning-module": "Baseline infrastructure creation and provisioning workflow capability",
    "network-foundation-module": "VPC, subnet, routing, gateway, VPN, WAN, and network path foundation capability",
    "compute-foundation-module": "Virtual machine, cloud instance, node, and runtime host foundation capability",
    "security-baseline-module": "Security group, access boundary, policy, and control baseline capability",
    "observability-foundation-module": "Metrics, logs, exporters, dashboards, and visibility foundation capability",
    "automation-execution-module": "Controlled script, runbook, configuration, and automation execution capability",
    "telemetry-aggregation-module": "Operational telemetry collection, normalization, and preparation capability",
    "dependency-correlation-module": "Signal, dependency, symptom, and impact path correlation capability",
    "recovery-orchestration-module": "Recovery, failover, restart, restoration, and mitigation orchestration capability",
    "validation-reporting-module": "Validation summary, evidence, manifest, and reporting capability",
    "continuity-governance-module": "Continuity decision, governance reporting, ownership, and executive evidence capability",
}

def title(slug: str) -> str:
    text = slug.replace("-module", "")
    return " ".join(part.capitalize() for part in text.split("-")) + " Module"

rows = []

for path in sorted(MODULE_ROOT.iterdir()):
    if not path.is_dir():
        continue

    slug = path.name
    rows.append({
        "slug": slug,
        "title": title(slug),
        "purpose": MODULE_DESCRIPTIONS.get(slug, "Reusable infrastructure and operational capability"),
    })

lines = [
    "# Operational Capability Modules",
    "",
    "This directory contains reusable infrastructure and operational capability modules.",
    "",
    "Modules are not individual scenarios. They define reusable capability boundaries used by build scenarios and lifecycle-based operational scenarios.",
    "",
    "---",
    "",
    "## Module Catalog",
    "",
    "| Module | Purpose |",
    "|---|---|",
]

for row in rows:
    lines.append(f"| [{row['title']}]({row['slug']}/) | {row['purpose']} |")

lines += [
    "",
    "---",
    "",
    "## Usage Model",
    "",
    "Build scenarios use modules to describe infrastructure construction and baseline configuration capabilities.",
    "",
    "Operational scenarios use modules to describe monitoring, correlation, recovery, validation, and continuity capabilities.",
    "",
    "---",
    "",
    "## Summary",
    "",
    "This module catalog provides reusable capability references for the infrastructure operations portfolio.",
    "",
]

OUTPUT.write_text("\n".join(lines), encoding="utf-8")
print(f"[OK] generated {OUTPUT}")
print(f"[OK] module count: {len(rows)}")
