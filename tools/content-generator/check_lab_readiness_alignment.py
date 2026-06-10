from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LABS_DIR = ROOT / "labs"
REPORT_PATH = ROOT / "reports" / "lab-readiness-alignment-check.md"

LABS = [
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

REQUIRED_PATHS = [
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

REQUIRED_TERMS = [
    "documentation-ready",
    "planned",
    "not yet executed",
    "placeholder until lab execution",
]

def read_text(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")

def main() -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Lab Readiness Alignment Check")
    lines.append("")
    lines.append("This report validates whether all implementation labs follow the expected documentation-ready boundary.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    total_missing = 0
    total_term_issues = 0

    detail = []

    for lab in LABS:
        lab_path = LABS_DIR / lab
        missing = []
        term_issues = []

        for rel in REQUIRED_PATHS:
            target = lab_path / rel
            if not target.exists():
                missing.append(rel)

        readme = read_text(lab_path / "README.md")
        metadata = read_text(lab_path / "lab-metadata.yaml")
        validation_report = read_text(lab_path / "validation-reports" / "lab-validation-report.md")

        combined = "\n".join([readme, metadata, validation_report]).lower()

        for term in REQUIRED_TERMS:
            if term.lower() not in combined:
                term_issues.append(term)

        total_missing += len(missing)
        total_term_issues += len(term_issues)

        status = "PASS" if not missing and not term_issues else "CHECK"

        lines.append(f"- {lab}: {status}")

        detail.append("")
        detail.append(f"## {lab}")
        detail.append("")
        detail.append(f"- Status: {status}")
        detail.append(f"- Missing required paths: {len(missing)}")
        detail.append(f"- Missing required status terms: {len(term_issues)}")
        detail.append("")

        if missing:
            detail.append("### Missing Paths")
            detail.append("")
            for item in missing:
                detail.append(f"- {item}")
            detail.append("")

        if term_issues:
            detail.append("### Missing Status Terms")
            detail.append("")
            for item in term_issues:
                detail.append(f"- {item}")
            detail.append("")

    lines.append("")
    lines.append("## Totals")
    lines.append("")
    lines.append(f"- Labs checked: {len(LABS)}")
    lines.append(f"- Missing required paths: {total_missing}")
    lines.append(f"- Missing required status terms: {total_term_issues}")
    lines.append("")
    lines.append("## Detailed Results")
    lines.extend(detail)

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] wrote {REPORT_PATH.relative_to(ROOT)}")
    print(f"[OK] labs checked: {len(LABS)}")
    print(f"[OK] missing required paths: {total_missing}")
    print(f"[OK] missing required status terms: {total_term_issues}")

    if total_missing or total_term_issues:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
