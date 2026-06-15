#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[2]
SCENARIOS_DIR = REPO / "scenarios"
LABS_DIR = REPO / "labs"
OUTPUT = REPO / "docs" / "lab-coverage-matrix.md"

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

LAB_SCOPE = {
    "01-linux-observability-lab": "Linux observability and host visibility",
    "02-network-routing-lab": "Network routing, reachability, DNS, and latency validation",
    "03-ansible-automation-lab": "Automation execution, recovery workflow, and validation",
    "04-container-runtime-lab": "Container runtime visibility and restart recovery",
    "05-kolla-openstack-lab": "OpenStack/Kolla-Ansible preflight and control plane readiness",
    "06-monitoring-stack-lab": "Prometheus/Grafana monitoring, scrape, and dashboard readiness",
    "07-logging-correlation-lab": "Log normalization, timeline reconstruction, and correlation analysis",
    "08-backup-recovery-lab": "Backup, restore, checksum, and integrity validation",
    "09-resilience-failover-lab": "Failover decision, traffic shift, and resilience validation",
    "10-governance-reporting-lab": "Repository validation, governance reporting, and quality gates",
}

def scenario_dirs(level_dir):
    path = SCENARIOS_DIR / level_dir
    if not path.exists():
        return []
    return sorted([p for p in path.iterdir() if p.is_dir()])

def classify_lab(scenario_name, level_dir):
    name = scenario_name.lower()

    if any(token in name for token in [
        "backup", "restore", "restoration", "data-protection", "replication", "storage-volume"
    ]):
        return "08-backup-recovery-lab"

    if any(token in name for token in [
        "failover", "resilience", "survivability", "continuity", "multi-region", "multi-site", "multi-cluster", "cross-region"
    ]):
        return "09-resilience-failover-lab"

    if any(token in name for token in [
        "governance", "report", "policy", "compliance"
    ]):
        return "10-governance-reporting-lab"

    if any(token in name for token in [
        "correlation", "analysis", "anomaly", "dependency", "risk", "threat", "timeline"
    ]):
        return "07-logging-correlation-lab"

    if any(token in name for token in [
        "prometheus", "grafana", "monitoring", "telemetry", "visibility", "health", "metric", "alert"
    ]):
        if any(network_token in name for network_token in [
            "vpn", "wan", "dns", "network", "routing", "packet", "latency", "connectivity", "endpoint"
        ]):
            return "02-network-routing-lab"
        if any(container_token in name for container_token in [
            "container", "kubernetes", "pod", "cluster", "service-mesh"
        ]):
            return "04-container-runtime-lab"
        if any(openstack_token in name for openstack_token in [
            "cloud", "control-plane", "platform"
        ]):
            return "05-kolla-openstack-lab"
        return "01-linux-observability-lab"

    if any(token in name for token in [
        "vpn", "wan", "dns", "network", "routing", "packet", "latency", "connectivity", "endpoint", "load-balancer"
    ]):
        return "02-network-routing-lab"

    if any(token in name for token in [
        "ansible", "automation", "rollback", "remediation", "orchestration", "rebalancing", "renewal"
    ]):
        return "03-ansible-automation-lab"

    if any(token in name for token in [
        "container", "kubernetes", "pod", "cluster", "service-mesh", "runtime"
    ]):
        return "04-container-runtime-lab"

    if any(token in name for token in [
        "openstack", "kolla", "cloud", "control-plane", "compute", "platform"
    ]):
        return "05-kolla-openstack-lab"

    if level_dir == "level-1-visibility":
        return "01-linux-observability-lab"
    if level_dir == "level-2-correlation":
        return "07-logging-correlation-lab"
    if level_dir == "level-3-recovery":
        return "03-ansible-automation-lab"
    if level_dir == "level-4-resilience":
        return "09-resilience-failover-lab"
    if level_dir == "level-5-continuity":
        return "10-governance-reporting-lab"

    return "10-governance-reporting-lab"

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    labs = [lab for lab in LAB_ORDER if (LABS_DIR / lab).exists()]
    coverage_rows = []
    level_counts = []
    lab_counts = {lab: 0 for lab in labs}

    total = 0

    for level_dir, level_name in LIFECYCLE_LEVELS:
        scenarios = scenario_dirs(level_dir)
        level_counts.append((level_dir, level_name, len(scenarios)))
        total += len(scenarios)

        for scenario in scenarios:
            lab = classify_lab(scenario.name, level_dir)

            if lab not in lab_counts:
                lab_counts[lab] = 0

            lab_counts[lab] += 1

            coverage_rows.append({
                "level_dir": level_dir,
                "level_name": level_name,
                "scenario": scenario.name,
                "lab": lab,
            })

    covered = sum(lab_counts.values())
    uncovered = total - covered

    lines = [
        "# Lab Coverage Matrix",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        "",
        "## Purpose",
        "",
        "This document maps lifecycle-aligned operational scenarios to implementation lab boundaries.",
        "",
        "Scenarios define operational validation cases.",
        "",
        "Labs define reusable implementation boundaries that validate groups of scenarios.",
        "",
        "This matrix is generated from repository state and scenario naming taxonomy.",
        "",
        "## Coverage Summary",
        "",
        "| Signal | Value |",
        "|---|---:|",
        f"| Total scenarios | {total} |",
        f"| Covered scenarios | {covered} |",
        f"| Uncovered scenarios | {uncovered} |",
        f"| Implementation labs | {len(labs)} |",
        "",
        "## Lifecycle Scenario Count",
        "",
        "| Lifecycle Level | Scenario Count |",
        "|---|---:|",
    ]

    for level_dir, level_name, count in level_counts:
        lines.append(f"| [{level_name}](../scenarios/{level_dir}/README.md) | {count} |")

    lines.extend([
        "",
        "## Lab Coverage Count",
        "",
        "| Lab | Scope | Covered Scenarios |",
        "|---|---|---:|",
    ])

    for lab in labs:
        lines.append(
            f"| [{lab}](../labs/{lab}/README.md) | {LAB_SCOPE.get(lab, 'Implementation boundary')} | {lab_counts.get(lab, 0)} |"
        )

    lines.extend([
        "",
        "## Scenario-to-Lab Matrix",
        "",
        "| Lifecycle Level | Scenario | Implementation Lab |",
        "|---|---|---|",
    ])

    for row in coverage_rows:
        lines.append(
            f"| {row['level_name']} | "
            f"[{row['scenario']}](../scenarios/{row['level_dir']}/{row['scenario']}/README.md) | "
            f"[{row['lab']}](../labs/{row['lab']}/README.md) |"
        )

    lines.extend([
        "",
        "## Mapping Policy",
        "",
        "The matrix maps scenarios to labs based on operational domain and scenario naming taxonomy.",
        "",
        "A scenario does not require a dedicated standalone lab.",
        "",
        "Multiple scenarios may be validated through the same reusable implementation boundary.",
        "",
        "This keeps the repository scalable while preserving reviewer-readable operational coverage.",
        "",
        "## Important Boundary",
        "",
        "This matrix represents implementation coverage at the lab boundary level.",
        "",
        "It does not claim that every scenario has a separate runtime deployment.",
        "",
        "Generated by tools/content-generator/generate_lab_coverage_matrix.py",
    ])

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] generated {OUTPUT}")
    print(f"[INFO] scenarios={total}")
    print(f"[INFO] covered={covered}")
    print(f"[INFO] uncovered={uncovered}")
    print(f"[INFO] labs={len(labs)}")

if __name__ == "__main__":
    main()