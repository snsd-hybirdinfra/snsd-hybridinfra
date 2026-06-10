from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "a.txt"

LABS = [
    ("01-linux-observability-lab", "Linux Observability Lab", "Linux host visibility, process health, filesystem state, service monitoring, and system events."),
    ("02-network-routing-lab", "Network Routing Lab", "Routing, VPN, WAN, DNS, reachability, latency, packet loss, and route recovery validation."),
    ("03-ansible-automation-lab", "Ansible Automation Lab", "Inventory, SSH access, playbook execution, rollback, recovery, validation, and automation evidence."),
    ("04-container-runtime-lab", "Container Runtime Lab", "Docker runtime visibility, container health, logs, restart recovery, and container evidence."),
    ("05-kolla-openstack-lab", "Kolla OpenStack Lab", "Kolla-Ansible based OpenStack control plane, compute, network, service recovery, and evidence."),
    ("06-monitoring-stack-lab", "Monitoring Stack Lab", "Prometheus, Grafana, exporter telemetry, dashboard readiness, alert readiness, and monitoring evidence."),
    ("07-logging-correlation-lab", "Logging Correlation Lab", "Log collection, event normalization, OpenSearch query readiness, correlation, timeline reconstruction, and evidence."),
    ("08-backup-recovery-lab", "Backup Recovery Lab", "Backup job readiness, artifact validation, restore workflows, integrity checks, and recovery evidence."),
    ("09-resilience-failover-lab", "Resilience Failover Lab", "Failure detection, failover decision, traffic shift validation, recovery validation, and resilience evidence."),
    ("10-governance-reporting-lab", "Governance Reporting Lab", "Repository validation, coverage reporting, quality gates, documentation consistency, and governance reporting."),
]

SCENARIO_LEVELS = [
    ("Level 1 Visibility", 45),
    ("Level 2 Correlation", 41),
    ("Level 3 Recovery", 33),
    ("Level 4 Resilience", 21),
    ("Level 5 Continuity", 10),
]

REQUIRED_LAB_PATHS = [
    "README.md",
    "lab-metadata.yaml",
    "architecture/implementation-plan.md",
    "modules",
    "adapters",
    "shared-runtime/README.md",
    "shared-runtime/runners/README.md",
    "shared-runtime/validators/README.md",
    "shared-runtime/parsers/README.md",
    "scripts/README.md",
    "scripts/setup.sh",
    "scripts/validate.sh",
    "scripts/cleanup.sh",
    "evidence/README.md",
    "evidence/raw/README.md",
    "evidence/processed/README.md",
    "evidence/summary/README.md",
    "validation-reports/scenario-coverage-report.md",
    "validation-reports/lab-validation-report.md",
]

def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_dir())

def count_files_by_name(root: Path, name: str) -> int:
    if not root.exists():
        return 0
    return sum(1 for item in root.rglob(name) if item.is_file())

def count_files_by_suffix(root: Path, suffix: str) -> int:
    if not root.exists():
        return 0
    return sum(1 for item in root.rglob(f"*{suffix}") if item.is_file())

def lab_missing_items(lab_name: str) -> list[str]:
    base = ROOT / "labs" / lab_name
    missing = []
    for rel in REQUIRED_LAB_PATHS:
        if not (base / rel).exists():
            missing.append(rel)
    return missing

def read_report_value(report_path: Path, label: str) -> str:
    if not report_path.exists():
        return "unknown"
    text = report_path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        if label in line:
            return line.strip()
    return "unknown"

def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    scenario_count = count_dirs(ROOT / "scenarios" / "level-1-visibility")
    scenario_count += count_dirs(ROOT / "scenarios" / "level-2-correlation")
    scenario_count += count_dirs(ROOT / "scenarios" / "level-3-recovery")
    scenario_count += count_dirs(ROOT / "scenarios" / "level-4-resilience")
    scenario_count += count_dirs(ROOT / "scenarios" / "level-5-continuity")

    lab_count = count_dirs(ROOT / "labs")
    metadata_count = count_files_by_name(ROOT / "scenarios", "metadata.yaml")
    poster_svg_count = count_files_by_name(ROOT / "scenarios", "operational-poster.svg")
    poster_png_count = count_files_by_name(ROOT / "scenarios", "operational-poster.png")

    missing_lab_total = 0
    lab_lines = []
    for lab_name, lab_title, focus in LABS:
        missing = lab_missing_items(lab_name)
        missing_lab_total += len(missing)
        status = "PASS" if not missing else f"CHECK missing={len(missing)}"
        lab_lines.append(f"- {lab_name} | {lab_title} | {status}")
        lab_lines.append(f"  Focus: {focus}")

    lines = []
    lines.append("SNSD HYBRID INFRASTRUCTURE - LOCAL EXECUTIVE SUMMARY")
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"Generated At: {now}")
    lines.append("File Role: Local-only executive repository summary")
    lines.append("Git Policy: a.txt is intentionally ignored and should not be committed")
    lines.append("")
    lines.append("1. Repository Positioning")
    lines.append("- Repository: SNSD Hybrid Infrastructure")
    lines.append("- Positioning: Enterprise Operational Capability Platform")
    lines.append("- Model: Scenario-driven Infrastructure Operations Portfolio")
    lines.append("- Purpose: Validate reusable operational capabilities through lifecycle-aligned scenarios and implementation-oriented labs")
    lines.append("- Important Boundary: This is not a simple scenario collection")
    lines.append("")
    lines.append("2. Operational Lifecycle")
    lines.append("- Detection")
    lines.append("- Correlation & Analysis")
    lines.append("- Incident Coordination")
    lines.append("- Recovery & Automation")
    lines.append("- Recovery Validation")
    lines.append("- Governance & Reporting")
    lines.append("")
    lines.append("3. Scenario Inventory")
    for level, count in SCENARIO_LEVELS:
        lines.append(f"- {level}: {count}")
    lines.append(f"- Total Scenarios: {scenario_count}")
    lines.append("")
    lines.append("4. Lab Inventory")
    lines.append(f"- Total Labs: {lab_count}")
    lines.append("- Lab Readiness: documentation-ready")
    lines.append("- Implementation Status: planned")
    lines.append("- Execution Status: not yet executed")
    lines.append("- Evidence Status: placeholder until lab execution")
    lines.append("")
    lines.extend(lab_lines)
    lines.append("")
    lines.append("5. Artifact Coverage")
    lines.append(f"- Scenario metadata files: {metadata_count}")
    lines.append(f"- Scenario poster SVG files: {poster_svg_count}")
    lines.append(f"- Scenario poster PNG files: {poster_png_count}")
    lines.append(f"- Missing required lab artifacts: {missing_lab_total}")
    lines.append("")
    lines.append("6. Report Layering")
    lines.append("- docs/: stable reviewer-facing repository documentation")
    lines.append("- reports/: generated detailed checker outputs for maintainers")
    lines.append("- validation-reports/: reviewer-facing validation summaries")
    lines.append("- a.txt: local-only executive summary")
    lines.append("")
    lines.append("7. Reviewer Entry Points")
    lines.append("- README.md")
    lines.append("- validation-reports/lab-readiness-summary.md")
    lines.append("- docs/lab-coverage-matrix.md")
    lines.append("- docs/repository-tree.md")
    lines.append("- docs/report-layer-guide.md")
    lines.append("- scenarios/README.md")
    lines.append("- labs/*/README.md")
    lines.append("")
    lines.append("8. Current Baseline")
    lines.append("- 150 lifecycle-aligned scenarios")
    lines.append("- 10 implementation labs")
    lines.append("- 10 lab implementation plans")
    lines.append("- 10 lab validation reports")
    lines.append("- 10 scenario coverage reports")
    lines.append("- 10 lab evidence boundaries")
    lines.append("- 10 lab script boundaries")
    lines.append("- Repository validation target: PASS")
    lines.append("")
    lines.append("9. Implementation Boundary")
    lines.append("- Current state is documentation-ready")
    lines.append("- Runtime implementation is planned")
    lines.append("- Actual execution evidence has not yet been produced")
    lines.append("- Future implementation should begin with foundational labs")
    lines.append("")
    lines.append("10. Recommended Implementation Order")
    lines.append("- 01-linux-observability-lab")
    lines.append("- 03-ansible-automation-lab")
    lines.append("- 06-monitoring-stack-lab")
    lines.append("- 04-container-runtime-lab")
    lines.append("- 07-logging-correlation-lab")
    lines.append("- 02-network-routing-lab")
    lines.append("- 05-kolla-openstack-lab")
    lines.append("- 08-backup-recovery-lab")
    lines.append("- 09-resilience-failover-lab")
    lines.append("- 10-governance-reporting-lab")
    lines.append("")
    lines.append("11. Operational Summary")
    lines.append("The repository now presents a complete documentation-ready portfolio baseline.")
    lines.append("Scenarios define operational validation cases.")
    lines.append("Labs define implementation boundaries.")
    lines.append("Modules, adapters, and shared runtime areas define capability and integration boundaries.")
    lines.append("The next major phase is executable lab implementation, starting with Linux observability.")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] wrote {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
