#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[2]
LABS_DIR = REPO / "labs"
OUTPUT = REPO / "validation-reports" / "lab-readiness-summary.md"

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

def exists(path):
    return path.exists()

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

def status_label(value):
    return "PASS" if value else "MISSING"

def lab_status(values):
    if all(values):
        return "documentation-ready"
    return "needs-attention"

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    labs = [lab for lab in LAB_ORDER if (LABS_DIR / lab).exists()]

    rows = []
    ready_count = 0
    missing_count = 0

    for lab in labs:
        lab_dir = LABS_DIR / lab

        readme_ok = exists(lab_dir / "README.md")
        scripts_ok = exists(lab_dir / "scripts") and has_required_scripts(lab_dir)
        validation_reports_ok = exists(lab_dir / "validation-reports")
        execution_note_ok = bool(find_execution_notes(lab_dir))
        runtime_assets_ok = has_runtime_boundary_assets(lab_dir)

        values = [
            readme_ok,
            scripts_ok,
            validation_reports_ok,
            execution_note_ok,
            runtime_assets_ok,
        ]

        status = lab_status(values)

        if status == "documentation-ready":
            ready_count += 1
        else:
            missing_count += 1

        rows.append({
            "lab": lab,
            "readme": status_label(readme_ok),
            "scripts": status_label(scripts_ok),
            "validation_reports": status_label(validation_reports_ok),
            "execution_note": status_label(execution_note_ok),
            "runtime_assets": status_label(runtime_assets_ok),
            "status": status,
        })

    lines = [
        "# Lab Readiness Summary",
        "",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        "",
        "## Purpose",
        "",
        "This document summarizes reviewer-facing readiness for implementation labs.",
        "",
        "It is generated from repository state and does not depend on local runtime evidence.",
        "",
        "## Readiness Counters",
        "",
        "| Counter | Value |",
        "|---|---:|",
        f"| Total implementation labs | {len(labs)} |",
        f"| Documentation-ready labs | {ready_count} |",
        f"| Labs needing attention | {missing_count} |",
        "",
        "## Readiness Matrix",
        "",
        "| Lab | README | Scripts | Validation Reports | Execution Note | Runtime Boundary Assets | Status |",
        "|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| [{row['lab']}](../labs/{row['lab']}/README.md) | "
            f"{row['readme']} | "
            f"{row['scripts']} | "
            f"{row['validation_reports']} | "
            f"{row['execution_note']} | "
            f"{row['runtime_assets']} | "
            f"{row['status']} |"
        )

    lines.extend([
        "",
        "## Readiness Policy",
        "",
        "A lab is considered documentation-ready when it has:",
        "",
        "- a lab README",
        "- setup, validation, and cleanup scripts",
        "- a validation-reports directory",
        "- an execution boundary note",
        "- at least one runtime boundary asset directory such as configs, compose, playbooks, inventory, datasets, or architecture",
        "",
        "Generated runtime evidence is intentionally excluded from this readiness check.",
        "",
        "## Important Boundary",
        "",
        "This summary validates repository readiness and reviewer-facing structure.",
        "",
        "It does not claim that every lab runtime has been executed in the current Git checkout.",
        "",
    ])

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] generated {OUTPUT}")
    print(f"[INFO] labs={len(labs)}")
    print(f"[INFO] documentation_ready={ready_count}")
    print(f"[INFO] needs_attention={missing_count}")

if __name__ == "__main__":
    main()