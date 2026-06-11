#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[2]
LABS_DIR = REPO / "labs"
OUTPUT = REPO / "validation-reports" / "lab-runtime-implementation-summary.md"

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

RUNTIME_BOUNDARY = {
    "01-linux-observability-lab": "Linux host visibility and node exporter preparation",
    "02-network-routing-lab": "Reachability, route, DNS, latency, and service path validation",
    "03-ansible-automation-lab": "SSH, sudo, package, service, marker, and validation automation",
    "04-container-runtime-lab": "Docker runtime, container health, endpoint, logs, and restart validation",
    "05-kolla-openstack-lab": "Kolla-Ansible preflight, inventory, globals, and command validation",
    "06-monitoring-stack-lab": "Prometheus, Grafana, target scrape, and dashboard provisioning validation",
    "07-logging-correlation-lab": "File-based log normalization, timeline reconstruction, and rule correlation",
    "08-backup-recovery-lab": "Filesystem backup, restore, checksum, and integrity validation",
    "09-resilience-failover-lab": "Failure detection, failover decision, traffic shift, and recovery validation",
    "10-governance-reporting-lab": "Runtime summary aggregation and governance matrix generation",
}

LIFECYCLE_SUPPORT = {
    "Detection": [
        "01-linux-observability-lab",
        "02-network-routing-lab",
        "04-container-runtime-lab",
        "06-monitoring-stack-lab",
    ],
    "Correlation & Analysis": [
        "06-monitoring-stack-lab",
        "07-logging-correlation-lab",
    ],
    "Incident Coordination": [
        "03-ansible-automation-lab",
        "07-logging-correlation-lab",
        "10-governance-reporting-lab",
    ],
    "Recovery & Automation": [
        "03-ansible-automation-lab",
        "08-backup-recovery-lab",
        "09-resilience-failover-lab",
    ],
    "Recovery Validation": [
        "02-network-routing-lab",
        "04-container-runtime-lab",
        "08-backup-recovery-lab",
        "09-resilience-failover-lab",
    ],
    "Governance & Reporting": [
        "10-governance-reporting-lab",
    ],
}

def read_text(path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

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

def lab_runtime_summary_name(lab_dir):
    summaries = find_runtime_summaries(lab_dir)
    if not summaries:
        return "not generated"
    return ", ".join(summary.name for summary in summaries)

def lab_runtime_status(lab_dir):
    summaries = find_runtime_summaries(lab_dir)
    if not summaries:
        return "not generated"

    statuses = [runtime_status_from_summary(summary) for summary in summaries]

    if "PASS" in statuses:
        return "PASS"
    if "FAIL" in statuses:
        return "FAIL"
    if "CHECK" in statuses:
        return "CHECK"
    return "local runtime present"

def lab_execution_note_status(lab_dir):
    notes = find_execution_notes(lab_dir)
    if not notes:
        return "not documented"
    return ", ".join(note.name for note in notes)

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    labs = [lab for lab in LAB_ORDER if (LABS_DIR / lab).exists()]

    runtime_pass_count = 0
    runtime_check_count = 0
    runtime_fail_count = 0
    runtime_present_count = 0
    runtime_missing_count = 0
    execution_note_count = 0

    rows = []

    for lab in labs:
        lab_dir = LABS_DIR / lab
        status = lab_runtime_status(lab_dir)
        summary_name = lab_runtime_summary_name(lab_dir)
        note_status = lab_execution_note_status(lab_dir)

        if note_status != "not documented":
            execution_note_count += 1

        if status == "PASS":
            runtime_pass_count += 1
        elif status == "CHECK":
            runtime_check_count += 1
        elif status == "FAIL":
            runtime_fail_count += 1
        elif status == "local runtime present":
            runtime_present_count += 1
        else:
            runtime_missing_count += 1

        rows.append((lab, RUNTIME_BOUNDARY.get(lab, "Implementation boundary"), summary_name, note_status, status))

    lines = [
        "# Lab Runtime Implementation Summary",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        "",
        "## Purpose",
        "",
        "This document summarizes the runtime implementation boundary of the ten implementation labs.",
        "",
        "The repository remains an Enterprise Operational Capability Platform.",
        "",
        "Each lab provides an implementation-oriented execution boundary that supports lifecycle-aligned operational scenarios.",
        "",
        "## Runtime Baseline Counters",
        "",
        "| Counter | Value |",
        "|---|---:|",
        f"| Total implementation labs | {len(labs)} |",
        f"| Labs with execution boundary notes | {execution_note_count} |",
        f"| Runtime PASS summaries | {runtime_pass_count} |",
        f"| Runtime CHECK summaries | {runtime_check_count} |",
        f"| Runtime FAIL summaries | {runtime_fail_count} |",
        f"| Runtime present summaries | {runtime_present_count} |",
        f"| Labs missing local runtime summary | {runtime_missing_count} |",
        "",
        "## Runtime Implementation Matrix",
        "",
        "| Lab | Runtime Boundary | Runtime Summary | Execution Boundary Note | Status |",
        "|---|---|---|---|---|",
    ]

    for lab, boundary, summary_name, note_status, status in rows:
        lines.append(
            f"| [{lab}](../labs/{lab}/README.md) | {boundary} | {summary_name} | {note_status} | {status} |"
        )

    lines.extend([
        "",
        "## Execution Boundary Policy",
        "",
        "Generated runtime evidence is local-only and is intentionally excluded from Git.",
        "",
        "Committed repository content records:",
        "",
        "- execution scripts",
        "- validation scripts",
        "- configuration examples",
        "- execution boundary notes",
        "- reviewer-facing validation reports",
        "",
        "Local-only evidence records:",
        "",
        "- raw command output",
        "- generated runtime summaries",
        "- runtime workspaces",
        "- temporary validation artifacts",
        "",
        "## Lifecycle Coverage",
        "",
        "The lab implementation boundaries support the repository lifecycle as follows:",
        "",
        "| Lifecycle Area | Supporting Labs |",
        "|---|---|",
    ])

    for lifecycle_area, supporting_labs in LIFECYCLE_SUPPORT.items():
        rendered = ", ".join(f"[{lab}](../labs/{lab}/README.md)" for lab in supporting_labs if lab in labs)
        lines.append(f"| {lifecycle_area} | {rendered} |")

    lines.extend([
        "",
        "## Current Implementation Baseline",
        "",
        "The current implementation baseline includes:",
        "",
        f"- {len(labs)} implementation labs",
        f"- {execution_note_count} execution boundary notes",
        f"- {runtime_pass_count} runtime PASS summaries",
        "- repository validation PASS target",
        "- scenario inventory coverage across 150 lifecycle-aligned scenarios",
        "",
        "## Important Boundary",
        "",
        "This repository does not claim production deployment of every technology stack.",
        "",
        "Instead, it validates reusable operational capability boundaries through controlled, reviewer-readable lab implementations.",
        "",
        "Generated by tools/content-generator/generate_lab_runtime_summary.py",
    ])

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] generated {OUTPUT}")
    print(f"[INFO] labs={len(labs)}")
    print(f"[INFO] execution_notes={execution_note_count}")
    print(f"[INFO] runtime_pass={runtime_pass_count}")

if __name__ == "__main__":
    main()