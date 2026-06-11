#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[2]
LABS_DIR = REPO / "labs"
OUTPUT = LABS_DIR / "README.md"

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
    "05-kolla-openstack-lab": "Kolla-Ansible based OpenStack control plane readiness, network model, service preflight, and validation evidence",
    "06-monitoring-stack-lab": "Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence",
    "07-logging-correlation-lab": "Log collection, event normalization, correlation, timeline reconstruction, and evidence",
    "08-backup-recovery-lab": "Backup job readiness, artifact validation, restore workflows, integrity checks, and recovery evidence",
    "09-resilience-failover-lab": "Failure detection, failover decision, traffic shift validation, recovery validation, and resilience evidence",
    "10-governance-reporting-lab": "Repository validation, coverage reporting, quality gates, documentation consistency, and governance reporting",
}

LAB_SCOPE = {
    "01-linux-observability-lab": "Observability",
    "02-network-routing-lab": "Network",
    "03-ansible-automation-lab": "Automation",
    "04-container-runtime-lab": "Container Runtime",
    "05-kolla-openstack-lab": "OpenStack Preflight",
    "06-monitoring-stack-lab": "Monitoring",
    "07-logging-correlation-lab": "Logging & Correlation",
    "08-backup-recovery-lab": "Backup & Recovery",
    "09-resilience-failover-lab": "Resilience",
    "10-governance-reporting-lab": "Governance",
}

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

def has_required_scripts(lab_dir):
    scripts = lab_dir / "scripts"
    if not scripts.exists():
        return False

    expected = [
        scripts / "setup.sh",
        scripts / "validate.sh",
        scripts / "cleanup.sh",
    ]

    return all(path.exists() for path in expected)

def has_runtime_boundary_assets(lab_dir):
    candidates = [
        lab_dir / "configs",
        lab_dir / "compose",
        lab_dir / "playbooks",
        lab_dir / "inventory",
        lab_dir / "datasets",
        lab_dir / "architecture",
    ]

    return any(path.exists() for path in candidates)

def readiness_status(lab_dir):
    checks = [
        (lab_dir / "README.md").exists(),
        has_required_scripts(lab_dir),
        (lab_dir / "validation-reports").exists(),
        bool(find_execution_notes(lab_dir)),
        has_runtime_boundary_assets(lab_dir),
    ]

    if all(checks):
        return "documentation-ready"
    return "needs-attention"

def status_mark(value):
    return "PASS" if value else "MISSING"

def main():
    labs = [lab for lab in LAB_ORDER if (LABS_DIR / lab).exists()]

    ready_count = 0
    needs_attention_count = 0

    rows = []

    for lab in labs:
        lab_dir = LABS_DIR / lab

        readme_ok = (lab_dir / "README.md").exists()
        scripts_ok = has_required_scripts(lab_dir)
        execution_note_ok = bool(find_execution_notes(lab_dir))
        runtime_assets_ok = has_runtime_boundary_assets(lab_dir)
        status = readiness_status(lab_dir)

        if status == "documentation-ready":
            ready_count += 1
        else:
            needs_attention_count += 1

        rows.append({
            "lab": lab,
            "scope": LAB_SCOPE.get(lab, "Implementation"),
            "focus": LAB_FOCUS.get(lab, "Implementation lab"),
            "readme": status_mark(readme_ok),
            "scripts": status_mark(scripts_ok),
            "execution_note": status_mark(execution_note_ok),
            "runtime_assets": status_mark(runtime_assets_ok),
            "status": status,
        })

    lines = [
        "# Implementation Labs",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        "",
        "## Purpose",
        "",
        "This directory contains implementation-oriented lab boundaries for validating lifecycle-aligned infrastructure operations scenarios.",
        "",
        "Labs are not isolated tutorials.",
        "",
        "They are reusable execution boundaries that support scenario validation across observability, automation, recovery, resilience, and governance workflows.",
        "",
        "## Lab Baseline",
        "",
        "| Signal | Value |",
        "|---|---:|",
        f"| Total implementation labs | {len(labs)} |",
        f"| Documentation-ready labs | {ready_count} |",
        f"| Labs needing attention | {needs_attention_count} |",
        "",
        "## Lab Index",
        "",
        "| Lab | Scope | Focus | Status |",
        "|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| [{row['lab']}](./{row['lab']}/README.md) | {row['scope']} | {row['focus']} | {row['status']} |"
        )

    lines.extend([
        "",
        "## Readiness Matrix",
        "",
        "| Lab | README | Scripts | Execution Note | Runtime Boundary Assets | Status |",
        "|---|---|---|---|---|---|",
    ])

    for row in rows:
        lines.append(
            f"| [{row['lab']}](./{row['lab']}/README.md) | "
            f"{row['readme']} | "
            f"{row['scripts']} | "
            f"{row['execution_note']} | "
            f"{row['runtime_assets']} | "
            f"{row['status']} |"
        )

    lines.extend([
        "",
        "## Execution Boundary Model",
        "",
        "Each lab provides a controlled implementation boundary for one or more operational capabilities.",
        "",
        "A lab boundary may include:",
        "",
        "- setup scripts",
        "- validation scripts",
        "- cleanup scripts",
        "- configuration examples",
        "- compose definitions",
        "- Ansible playbooks",
        "- datasets",
        "- architecture notes",
        "- execution boundary notes",
        "",
        "## Runtime Evidence Policy",
        "",
        "Generated lab runtime evidence is local-only and intentionally excluded from Git.",
        "",
        "Committed lab content should remain reviewer-readable and environment-neutral.",
        "",
        "Local-only runtime content includes:",
        "",
        "- raw command output",
        "- generated runtime summaries",
        "- temporary runtime workspaces",
        "- sensitive local execution artifacts",
        "",
        "## Related Repository Documents",
        "",
        "- [Lab Runtime Implementation Summary](../validation-reports/lab-runtime-implementation-summary.md)",
        "- [Lab Readiness Summary](../validation-reports/lab-readiness-summary.md)",
        "- [Lab Coverage Matrix](../docs/lab-coverage-matrix.md)",
        "- [Repository README](../README.md)",
        "",
        "Generated by tools/content-generator/generate_labs_readme.py",
    ])

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] generated {OUTPUT}")
    print(f"[INFO] labs={len(labs)}")
    print(f"[INFO] documentation_ready={ready_count}")
    print(f"[INFO] needs_attention={needs_attention_count}")

if __name__ == "__main__":
    main()