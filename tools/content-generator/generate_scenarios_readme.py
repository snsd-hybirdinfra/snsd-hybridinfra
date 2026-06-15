#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[2]
SCENARIOS_DIR = REPO / "scenarios"
OUTPUT = SCENARIOS_DIR / "README.md"

LIFECYCLE_LEVELS = [
    ("level-1-visibility", "Level 1 Visibility", "Detection and visibility-oriented operational scenarios"),
    ("level-2-correlation", "Level 2 Correlation", "Correlation, dependency analysis, and anomaly reasoning scenarios"),
    ("level-3-recovery", "Level 3 Recovery", "Recovery automation and restoration workflow scenarios"),
    ("level-4-resilience", "Level 4 Resilience", "Distributed resilience, failover, and survivability scenarios"),
    ("level-5-continuity", "Level 5 Continuity", "Enterprise continuity and governance-aligned operational scenarios"),
]

def scenario_dirs(level_dir):
    path = SCENARIOS_DIR / level_dir
    if not path.exists():
        return []
    return sorted([p for p in path.iterdir() if p.is_dir()])

def count_files_under(path, pattern):
    if not path.exists():
        return 0
    return len(list(path.glob(pattern)))

def has_readme(path):
    return (path / "README.md").exists()

def has_generated_evidence(path):
    evidence_dir = path / "evidence" / "generated"
    if not evidence_dir.exists():
        return False

    required = [
        evidence_dir / "summary.md",
        evidence_dir / "execution-evidence.md",
        evidence_dir / "validation-evidence.md",
        evidence_dir / "artifact-manifest.json",
        evidence_dir / "artifact-checksums.json",
    ]

    return all(p.exists() for p in required)

def scenario_status(path):
    checks = [
        has_readme(path),
        has_generated_evidence(path),
    ]
    if all(checks):
        return "ready"
    return "needs-attention"

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    level_rows = []
    scenario_rows = []

    total_scenarios = 0
    total_ready = 0
    total_needs_attention = 0

    total_svg = count_files_under(SCENARIOS_DIR, "**/*.svg")
    total_png = count_files_under(SCENARIOS_DIR, "**/*.png")
    total_summary = count_files_under(SCENARIOS_DIR, "**/evidence/generated/summary.md")
    total_execution = count_files_under(SCENARIOS_DIR, "**/evidence/generated/execution-evidence.md")
    total_validation = count_files_under(SCENARIOS_DIR, "**/evidence/generated/validation-evidence.md")

    for level_dir, level_name, description in LIFECYCLE_LEVELS:
        scenarios = scenario_dirs(level_dir)
        count = len(scenarios)
        total_scenarios += count

        ready = 0
        needs_attention = 0

        for scenario in scenarios:
            status = scenario_status(scenario)
            if status == "ready":
                ready += 1
                total_ready += 1
            else:
                needs_attention += 1
                total_needs_attention += 1

            scenario_rows.append((level_name, level_dir, scenario.name, status))

        level_rows.append((level_dir, level_name, description, count, ready, needs_attention))

    lines = [
        "# Scenario Inventory",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        "",
        "## Purpose",
        "",
        "This directory contains lifecycle-aligned operational scenarios for SNSD Hybrid Infrastructure.",
        "",
        "Scenarios are operational validation cases, not isolated troubleshooting notes.",
        "",
        "They describe how infrastructure operations are detected, correlated, coordinated, recovered, validated, and reported.",
        "",
        "## Scenario Baseline",
        "",
        "| Signal | Value |",
        "|---|---:|",
        f"| Total scenarios | {total_scenarios} |",
        f"| Ready scenarios | {total_ready} |",
        f"| Scenarios needing attention | {total_needs_attention} |",
        f"| Scenario poster SVG artifacts | {total_svg} |",
        f"| Scenario poster PNG artifacts | {total_png} |",
        f"| Generated summary evidence files | {total_summary} |",
        f"| Generated execution evidence files | {total_execution} |",
        f"| Generated validation evidence files | {total_validation} |",
        "",
        "## Lifecycle Levels",
        "",
        "| Lifecycle Level | Description | Scenario Count | Ready | Needs Attention |",
        "|---|---|---:|---:|---:|",
    ]

    for level_dir, level_name, description, count, ready, needs_attention in level_rows:
        lines.append(
            f"| [{level_name}](./{level_dir}/README.md) | {description} | {count} | {ready} | {needs_attention} |"
        )

    lines.extend([
        "",
        "## Scenario Index",
        "",
        "| Level | Scenario | Status |",
        "|---|---|---|",
    ])

    for level_name, level_dir, scenario_name, status in scenario_rows:
        lines.append(
            f"| {level_name} | [{scenario_name}](./{level_dir}/{scenario_name}/README.md) | {status} |"
        )

    lines.extend([
        "",
        "## Scenario Evidence Policy",
        "",
        "Scenario evidence under `scenarios/*/evidence/generated/` is committed as reviewer-readable placeholder evidence.",
        "",
        "This differs from lab runtime evidence, which is generated locally and intentionally excluded from Git.",
        "",
        "See [Runtime Evidence Policy](../docs/runtime-evidence-policy.md) for the full evidence classification.",
        "",
        "Scenario evidence provides stable links for:",
        "",
        "- execution evidence",
        "- validation evidence",
        "- scenario summary evidence",
        "- artifact manifests",
        "- artifact checksums",
        "",
        "## Relationship to Labs",
        "",
        "Scenarios define operational validation cases.",
        "",
        "Labs define implementation boundaries for validating groups of scenarios.",
        "",
        "See:",
        "",
        "- [Implementation Labs](../labs/README.md)",
        "- [Lab Coverage Matrix](../docs/lab-coverage-matrix.md)",
        "- [Lab Runtime Implementation Summary](../validation-reports/lab-runtime-implementation-summary.md)",
        "- [Runtime Evidence Policy](../docs/runtime-evidence-policy.md)",
        "",
        "## Important Boundary",
        "",
        "The scenario inventory represents lifecycle coverage and reviewer-facing operational modeling.",
        "",
        "It does not mean each scenario is implemented as a separate standalone runtime lab.",
        "",
    ])

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] generated {OUTPUT}")
    print(f"[INFO] scenarios={total_scenarios}")
    print(f"[INFO] ready={total_ready}")
    print(f"[INFO] needs_attention={total_needs_attention}")
    print(f"[INFO] svg={total_svg}")
    print(f"[INFO] png={total_png}")

if __name__ == "__main__":
    main()