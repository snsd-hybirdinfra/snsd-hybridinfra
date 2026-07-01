from pathlib import Path
import sys

ROOT = Path(".").resolve()
LABS = ROOT / "labs"
REPORT = ROOT / "validation-reports" / "lab-validation-summary.md"

EXPECTED_LABS = [
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

REQUIRED_ITEMS = [
    "README.md",
    "lab-metadata.yaml",
    "architecture",
    "architecture/lab-architecture.md",
    "modules",
    "adapters",
    "shared-runtime",
    "shared-runtime/README.md",
    "shared-runtime/runners",
    "shared-runtime/validators",
    "shared-runtime/parsers",
    "scenarios",
    "evidence",
    "evidence/raw",
    "evidence/processed",
    "evidence/summary",
    "validation-reports",
    "validation-reports/lab-validation-report.md",
    "validation-reports/scenario-coverage-report.md",
    "scripts",
    "scripts/setup.sh",
    "scripts/validate.sh",
    "scripts/cleanup.sh",
]

missing = []

for lab in EXPECTED_LABS:
    lab_dir = LABS / lab

    if not lab_dir.exists():
        missing.append(f"{lab}/")
        continue

    for item in REQUIRED_ITEMS:
        target = lab_dir / item
        if not target.exists():
            missing.append(f"{lab}/{item}")

lines = []
lines.append("# Lab Validation Summary")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("expected_labs: " + str(len(EXPECTED_LABS)))
lines.append("missing_lab_items: " + str(len(missing)))
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Missing Lab Items")
lines.append("")

if missing:
    for item in missing:
        lines.append("- " + item)
else:
    lines.append("NONE")

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("[OK] wrote validation-reports/lab-validation-summary.md")
print("[OK] expected labs: " + str(len(EXPECTED_LABS)))
print("[OK] missing lab items: " + str(len(missing)))

if missing:
    sys.exit(1)
