#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[2]
README = REPO / "README.md"

SCENARIOS_DIR = REPO / "scenarios"
LABS_DIR = REPO / "labs"
VALIDATION_REPORTS_DIR = REPO / "validation-reports"
REPORTS_DIR = REPO / "reports"

LIFECYCLE_LEVELS = [
    ("level-1-visibility", "Level 1 Visibility"),
    ("level-2-correlation", "Level 2 Correlation"),
    ("level-3-recovery", "Level 3 Recovery"),
    ("level-4-resilience", "Level 4 Resilience"),
    ("level-5-continuity", "Level 5 Continuity"),
]

LAB_ORDER = [
    "01-linux-observability-lab",
    "02-network-routing-lab",
    "03-ansible-automation-lab",
    "04-container-runtime-lab",
    "05-kolla-openstack-lab",
    "06-monitoring-stack-lab",
    "07-logging-correlation-lab",
    "08-backup-recovery-lab",
    "09-resilience-failover-lab",
    "10-governance-reporting-lab",
]

LAB_FOCUS = {
    "01-linux-observability-lab": "Linux host visibility, process health, filesystem state, service monitoring, and system events",
    "02-network-routing-lab": "Routing, VPN, WAN, DNS, reachability, latency, packet loss, and route recovery validation",
    "03-ansible-automation-lab": "Inventory, SSH access, playbook execution, rollback, recovery, validation, and automation evidence",
    "04-container-runtime-lab": "Docker runtime visibility, container health, logs, restart recovery, and container evidence",
    "05-kolla-openstack-lab": "Kolla-Ansible based OpenStack control plane, compute, network, service recovery, and evidence",
    "06-monitoring-stack-lab": "Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence",
    "07-logging-correlation-lab": "Log collection, event normalization, OpenSearch query readiness, correlation, timeline reconstruction, and evidence",
    "08-backup-recovery-lab": "Backup job readiness, artifact validation, restore workflows, integrity checks, and recovery evidence",
    "09-resilience-failover-lab": "Failure detection, failover decision, traffic shift validation, recovery validation, and resilience evidence",
    "10-governance-reporting-lab": "Repository validation, coverage reporting, quality gates, documentation consistency, and governance reporting",
}

RUNTIME_BOUNDARY = {
    "01-linux-observability-lab": "Linux host visibility and node exporter preparation",
    "02-network-routing-lab": "Route, DNS, latency, reachability, and service path validation",
    "03-ansible-automation-lab": "SSH, sudo, package, service, and playbook validation",
    "04-container-runtime-lab": "Docker runtime, container health, endpoint, log, and restart validation",
    "05-kolla-openstack-lab": "Kolla-Ansible preflight, inventory, globals, and command validation",
    "06-monitoring-stack-lab": "Prometheus, Grafana, target scrape, and dashboard provisioning validation",
    "07-logging-correlation-lab": "Log normalization, timeline reconstruction, and correlation validation",
    "08-backup-recovery-lab": "Backup, restore, checksum, and integrity validation",
    "09-resilience-failover-lab": "Failure detection, failover decision, traffic shift, and recovery validation",
    "10-governance-reporting-lab": "Runtime summary aggregation and governance matrix validation",
}

def read_text(path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def scenario_count(level_dir):
    path = SCENARIOS_DIR / level_dir
    if not path.exists():
        return 0
    return len([p for p in path.iterdir() if p.is_dir()])

def count_files(pattern):
    return len(list(REPO.glob(pattern)))

def find_execution_notes(lab_dir):
    report_dir = lab_dir / "validation-reports"
    if not report_dir.exists():
        return []

    patterns = [
        "*execution-note.md",
        "*execution-boundary*.md",
        "local-execution-note.md",
    ]

    found = []
    for pattern in patterns:
        found.extend(report_dir.glob(pattern))

    return sorted(set(found))

def find_runtime_summaries(lab_dir):
    summary_dir = lab_dir / "evidence" / "generated" / "summary"
    if not summary_dir.exists():
        return []
    return sorted(summary_dir.glob("*.md"))

def runtime_status_from_summary(path):
    text = read_text(path)
    if "Overall Status: PASS" in text or "Execution Status: PASS" in text:
        return "PASS"
    if "Overall Status: FAIL" in text or "Execution Status: FAIL" in text:
        return "FAIL"
    if "Overall Status: CHECK" in text or "Execution Status: CHECK" in text:
        return "CHECK"
    if text.strip():
        return "local runtime present"
    return "not generated"

def lab_runtime_status(lab_name):
    lab_dir = LABS_DIR / lab_name
    summaries = find_runtime_summaries(lab_dir)

    if not summaries:
        return "not generated"

    statuses = [runtime_status_from_summary(path) for path in summaries]

    if "PASS" in statuses:
        return "PASS"
    if "FAIL" in statuses:
        return "FAIL"
    if "CHECK" in statuses:
        return "CHECK"
    return "local runtime present"

def report_value(report_name, labels):
    path = REPORTS_DIR / report_name
    text = read_text(path)

    for label in labels:
        for line in text.splitlines():
            if label in line:
                value = line.split(":", 1)[-1].strip()
                if value:
                    return value

    return "not reported"

def root_quality_rows():
    rows = [
        ("missing_required_artifacts", report_value("portfolio-health-summary.md", ["Missing required artifacts"])),
        ("small_png_count", report_value("portfolio-health-summary.md", ["Small PNG count"])),
        ("markdown_broken_links", report_value("markdown-link-check.md", ["Broken links", "broken_links"])),
        ("top_level_extra_directories", report_value("top-level-structure-check.md", ["Extra directories", "extra_directories"])),
        ("top_level_missing_directories", report_value("top-level-structure-check.md", ["Missing directories", "missing_directories"])),
        ("root_readme_missing_links", report_value("root-readme-alignment-check.md", ["Missing links", "missing_links"])),
        ("root_readme_missing_terms", report_value("root-readme-alignment-check.md", ["Missing terms", "missing_terms"])),
        ("repository_language_hits", report_value("repository-language-check.md", ["Bad pattern hits", "repository_language_hits"])),
    ]
    return rows

def main():
    level_counts = [(label, scenario_count(level_dir)) for level_dir, label in LIFECYCLE_LEVELS]
    total_scenarios = sum(count for _, count in level_counts)

    labs = [lab for lab in LAB_ORDER if (LABS_DIR / lab).exists()]
    execution_note_count = sum(1 for lab in labs if find_execution_notes(LABS_DIR / lab))

    svg_count = count_files("scenarios/**/*.svg")
    png_count = count_files("scenarios/**/*.png")

    lines = [
        "# SNSD Hybrid Infrastructure",
        "",
        "Scenario-driven Infrastructure Operations Platform",
        "",
        "## Executive Overview",
        "",
        "SNSD Hybrid Infrastructure is an Enterprise Operational Capability Platform for scenario-driven infrastructure operations.",
        "",
        "This repository is not a simple scenario collection.",
        "",
        "It models reusable enterprise operational capabilities through lifecycle-aligned scenarios and validates them through implementation-oriented labs.",
        "",
        "The repository is organized around:",
        "",
        "- lifecycle-aligned operational scenarios",
        "- implementation labs",
        "- reusable module and adapter catalogs",
        "- shared runtime boundaries",
        "- reviewer-facing validation reports",
        "- local-only runtime evidence",
        "",
        "## Repository Positioning",
        "",
        "This repository is positioned as an:",
        "",
        "**Enterprise Operational Capability Platform**",
        "",
        "Scenarios define operational validation cases.",
        "",
        "Labs define implementation boundaries for validating those scenarios.",
        "",
        "Modules, adapters, and shared runtime directories define reusable capability catalogs and lab-local execution boundaries.",
        "",
        "## Operational Lifecycle",
        "",
        "Detection → Correlation & Analysis → Incident Coordination → Recovery & Automation → Recovery Validation → Governance & Reporting",
        "",
        "## Current Baseline",
        "",
        "| Area | Count / Status |",
        "|---|---:|",
        f"| Lifecycle-aligned scenarios | {total_scenarios} |",
        f"| Implementation labs | {len(labs)} |",
        f"| Execution boundary notes | {execution_note_count} |",
        "| Scenario levels | 5 |",
        "| Operational lifecycle stages | 6 |",
        f"| Scenario poster SVG artifacts | {svg_count} |",
        f"| Scenario poster PNG artifacts | {png_count} |",
        "| Repository validation target | PASS |",
        "",
        "## Runtime Implementation Baseline",
        "",
        "The current implementation baseline provides execution boundaries for implementation labs.",
        "",
        "| Lab | Runtime Boundary | Runtime Status |",
        "|---|---|---|",
    ]

    for lab in labs:
        lines.append(
            f"| [{lab}](./labs/{lab}/README.md) | {RUNTIME_BOUNDARY.get(lab, 'Implementation boundary')} | {lab_runtime_status(lab)} |"
        )

    lines.extend([
        "",
        "## Reviewer Quick Start",
        "",
        "Recommended review order:",
        "",
        "1. [Lab Runtime Implementation Summary](./validation-reports/lab-runtime-implementation-summary.md)",
        "2. [Lab Readiness Summary](./validation-reports/lab-readiness-summary.md)",
        "3. [Lab Coverage Matrix](./docs/lab-coverage-matrix.md)",
        "4. [Scenario Index](./scenarios/README.md)",
        "5. [Implementation Labs](./labs/README.md)",
        "6. [Report Layer Guide](./docs/report-layer-guide.md)",
        "7. [Repository Tree](./docs/repository-tree.md)",
        "8. [Runtime Evidence Policy](./docs/runtime-evidence-policy.md)",
        "9. [Phase 2 Backlog](./docs/phase-2-backlog.md)",
        "",
        "## Runtime Evidence Policy",
        "",
        "Runtime evidence is generated locally and intentionally excluded from Git.",
        "",
        "See [Runtime Evidence Policy](./docs/runtime-evidence-policy.md) for the scenario evidence and lab runtime evidence boundary.",
        "",
        "Committed content includes:",
        "",
        "- lab execution scripts",
        "- validation scripts",
        "- configuration examples",
        "- execution boundary notes",
        "- reviewer-facing validation reports",
        "- repository quality reports",
        "",
        "Local-only content includes:",
        "",
        "- raw command output",
        "- generated runtime summaries",
        "- temporary runtime workspaces",
        "- sensitive local execution artifacts",
        "",
        "## Scenario Inventory",
        "",
        "<!-- SCENARIO_INVENTORY_START -->",
        "| Lifecycle Level | Scenario Count |",
        "|---|---:|",
    ])

    for label, count in level_counts:
        lines.append(f"| {label} | {count} |")

    lines.extend([
        f"| Total | {total_scenarios} |",
        "<!-- SCENARIO_INVENTORY_END -->",
        "",
        "## Implementation Labs",
        "",
        "| Lab | Focus |",
        "|---|---|",
    ])

    for lab in labs:
        lines.append(f"| [{lab}](./labs/{lab}/README.md) | {LAB_FOCUS.get(lab, 'Implementation lab')} |")

    lines.extend([
        "",
        "## Report Layers",
        "",
        "| Directory | Role |",
        "|---|---|",
        "| [reports/](./reports/) | Generated detailed checker outputs |",
        "| [validation-reports/](./validation-reports/) | Reviewer-facing validation summaries |",
        "| [docs/](./docs/) | Reviewer-facing repository documentation |",
        "| [labs/](./labs/) | Implementation-oriented lab boundaries |",
        "| [scenarios/](./scenarios/) | Lifecycle-aligned operational validation scenarios |",
        "| [modules/](./modules/) | Repository-level capability module catalog |",
        "| [adapters/](./adapters/) | Repository-level adapter catalog |",
        "| [shared-runtime/](./shared-runtime/) | Shared runtime and integration boundary catalog |",
        "",
        "## Repository Support Areas",
        "",
        "- [Tools](./tools/) - repository generation, validation, and content automation utilities",
        "- [Builds](./builds/) - generated build and portfolio artifact index area",
        "- [Diagrams](./diagrams/) - repository-level visualization and diagram artifact area",
        "- [Internal](./internal/) - internal quality models, governance references, and repository control documents",
        "",
        "## Quality Status",
        "",
        "<!-- QUALITY_STATUS_START -->",
        "| Quality Signal | Current Value |",
        "|---|---|",
    ])

    for key, value in root_quality_rows():
        lines.append(f"| {key} | {value} |")

    lines.extend([
        "<!-- QUALITY_STATUS_END -->",
        "",
        "## Important Boundary",
        "",
        "This repository does not claim production deployment of every technology stack.",
        "",
        "It validates reusable operational capability boundaries through controlled, reviewer-readable lab implementations and lifecycle-aligned scenarios.",
        "",
        f"Generated by tools/content-generator/generate_root_readme.py",
    ])

    README.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] generated {README}")
    print(f"[INFO] scenarios={total_scenarios}")
    print(f"[INFO] labs={len(labs)}")
    print(f"[INFO] execution_boundary_notes={execution_note_count}")

if __name__ == "__main__":
    main()