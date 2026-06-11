from pathlib import Path
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "a.txt"

SCENARIO_LEVELS = [
    ("level-1-visibility", "Level 1 Visibility"),
    ("level-2-correlation", "Level 2 Correlation"),
    ("level-3-recovery", "Level 3 Recovery"),
    ("level-4-resilience", "Level 4 Resilience"),
    ("level-5-continuity", "Level 5 Continuity"),
]

IMPLEMENTATION_ORDER = [
    "01-linux-observability-lab",
    "03-ansible-automation-lab",
    "06-monitoring-stack-lab",
    "04-container-runtime-lab",
    "07-logging-correlation-lab",
    "02-network-routing-lab",
    "05-kolla-openstack-lab",
    "08-backup-recovery-lab",
    "09-resilience-failover-lab",
    "10-governance-reporting-lab",
]

def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")

def count_dirs(path):
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_dir())

def count_files(pattern):
    return sum(1 for _ in ROOT.glob(pattern))

def get_report_value(report_path, keys, default="not reported"):
    text = read_text(report_path)

    for key in keys:
        patterns = [
            rf"{re.escape(key)}\s*:\s*([0-9]+)",
            rf"\|\s*{re.escape(key)}\s*\|\s*([0-9]+)\s*\|",
            rf"{re.escape(key)}.*?([0-9]+)",
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)

    return default

def get_metadata_value(lab_dir, key, default="not reported"):
    text = read_text(lab_dir / "lab-metadata.yaml")
    match = re.search(rf"^{re.escape(key)}\s*:\s*(.+)$", text, re.IGNORECASE | re.MULTILINE)

    if match:
        return match.group(1).strip().strip('"').strip("'")

    return default

def get_lab_title(lab_dir):
    for key in ["lab_title", "title", "name"]:
        value = get_metadata_value(lab_dir, key, "")
        if value:
            return value

    readme = read_text(lab_dir / "README.md")
    match = re.search(r"^#\s+(.+)$", readme, re.MULTILINE)
    if match:
        return match.group(1).strip()

    return lab_dir.name

def get_lab_focus(lab_dir):
    text = read_text(lab_dir / "README.md")
    match = re.search(r"## Lab Focus\s+(.+?)(?:\n## |\Z)", text, re.IGNORECASE | re.DOTALL)

    if not match:
        return "not reported"

    lines = []
    for line in match.group(1).splitlines():
        line = line.strip().strip("-").strip()
        if line:
            lines.append(line)

    focus = " ".join(lines)
    if len(focus) > 220:
        return focus[:217] + "..."

    return focus if focus else "not reported"

def get_execution_notes(lab_dir):
    report_dir = lab_dir / "validation-reports"
    if not report_dir.exists():
        return []

    patterns = [
        "*execution-note.md",
        "*execution-boundary*.md",
        "local-execution-note.md",
        "monitoring-stack-execution-note.md",
    ]

    found = []
    for pattern in patterns:
        found.extend(report_dir.glob(pattern))

    unique = sorted(set(found))
    return unique

def has_execution_note(lab_dir):
    return len(get_execution_notes(lab_dir)) > 0

def get_execution_note_names(lab_dir):
    notes = get_execution_notes(lab_dir)
    if not notes:
        return "none"
    return ", ".join(note.name for note in notes)

def get_runtime_summary_files(lab_dir):
    summary_dir = lab_dir / "evidence" / "generated" / "summary"
    if not summary_dir.exists():
        return []
    return sorted(summary_dir.glob("*.md"))

def get_runtime_summary_status(lab_dir):
    files = get_runtime_summary_files(lab_dir)
    if not files:
        return "no local runtime summary"

    statuses = []
    for file_path in files:
        text = read_text(file_path)
        if "Overall Status: PASS" in text or "Execution Status: PASS" in text:
            statuses.append(f"{file_path.name}: PASS")
        elif "Overall Status: CHECK" in text or "Execution Status: CHECK" in text:
            statuses.append(f"{file_path.name}: CHECK")
        else:
            statuses.append(f"{file_path.name}: present")

    return ", ".join(statuses)

def get_labs():
    labs_root = ROOT / "labs"
    if not labs_root.exists():
        return []
    return sorted([item for item in labs_root.iterdir() if item.is_dir()])

def get_scenario_inventory():
    rows = []
    for dirname, label in SCENARIO_LEVELS:
        rows.append((label, count_dirs(ROOT / "scenarios" / dirname)))
    return rows

def get_validation_values():
    return {
        "missing_required_artifacts": get_report_value(
            ROOT / "reports" / "repository-quality-check.md",
            ["missing_required_artifacts", "missing required artifacts"],
        ),
        "small_png_count": get_report_value(
            ROOT / "reports" / "repository-quality-check.md",
            ["small_png_count", "small png count"],
        ),
        "markdown_broken_links": get_report_value(
            ROOT / "reports" / "markdown-link-check.md",
            ["broken_links", "broken links"],
        ),
        "top_level_missing_directories": get_report_value(
            ROOT / "reports" / "top-level-structure-check.md",
            ["missing_expected_directories", "missing dirs"],
        ),
        "top_level_extra_directories": get_report_value(
            ROOT / "reports" / "top-level-structure-check.md",
            ["extra_top_level_directories", "extra dirs"],
        ),
        "top_level_missing_readme_mentions": get_report_value(
            ROOT / "reports" / "top-level-structure-check.md",
            ["missing_root_readme_mentions"],
        ),
        "root_readme_missing_links": get_report_value(
            ROOT / "reports" / "root-readme-alignment-check.md",
            ["root_readme_missing_links"],
        ),
        "root_readme_missing_terms": get_report_value(
            ROOT / "reports" / "root-readme-alignment-check.md",
            ["root_readme_missing_terms"],
        ),
        "repository_language_hits": get_report_value(
            ROOT / "reports" / "repository-language-check.md",
            ["bad_pattern_hits", "repository_language_hits"],
        ),
        "lab_missing_required_paths": get_report_value(
            ROOT / "reports" / "lab-readiness-alignment-check.md",
            ["missing required paths", "missing_required_paths"],
        ),
        "lab_missing_status_terms": get_report_value(
            ROOT / "reports" / "lab-readiness-alignment-check.md",
            ["missing required status terms", "missing_required_status_terms"],
        ),
    }

def get_validation_status(values):
    blocking_keys = [
        "missing_required_artifacts",
        "markdown_broken_links",
        "top_level_missing_directories",
        "top_level_extra_directories",
        "top_level_missing_readme_mentions",
        "root_readme_missing_links",
        "root_readme_missing_terms",
        "repository_language_hits",
        "lab_missing_required_paths",
        "lab_missing_status_terms",
    ]

    for key in blocking_keys:
        value = values.get(key, "not reported")
        if value not in ["0", "not reported"]:
            return "CHECK"

    return "PASS"

def build_summary():
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    scenario_rows = get_scenario_inventory()
    total_scenarios = sum(count for _, count in scenario_rows)

    labs = get_labs()
    values = get_validation_values()
    validation_status = get_validation_status(values)

    execution_note_labs = [lab.name for lab in labs if has_execution_note(lab)]

    lines = []
    lines.append("SNSD HYBRID INFRASTRUCTURE - LOCAL EXECUTIVE SUMMARY")
    lines.append("========================================================================")
    lines.append("")
    lines.append(f"Generated At: {generated_at}")
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
    for item in [
        "Detection",
        "Correlation & Analysis",
        "Incident Coordination",
        "Recovery & Automation",
        "Recovery Validation",
        "Governance & Reporting",
    ]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("3. Scenario Inventory")
    for label, count in scenario_rows:
        lines.append(f"- {label}: {count}")
    lines.append(f"- Total Scenarios: {total_scenarios}")
    lines.append("")

    lines.append("4. Lab Inventory")
    lines.append(f"- Total Labs: {len(labs)}")
    lines.append(f"- Labs with execution boundary note: {len(execution_note_labs)}")
    lines.append(f"- Repository validation target: {validation_status}")
    lines.append("")

    for lab in labs:
        lines.append(f"- {lab.name} | {get_lab_title(lab)}")
        lines.append(f"  Documentation Status: {get_metadata_value(lab, 'documentation_status', get_metadata_value(lab, 'status'))}")
        lines.append(f"  Implementation Status: {get_metadata_value(lab, 'implementation_status')}")
        lines.append(f"  Execution Status: {get_metadata_value(lab, 'execution_status')}")
        lines.append(f"  Evidence Status: {get_metadata_value(lab, 'evidence_status')}")
        lines.append(f"  Execution Boundary Note: {get_execution_note_names(lab)}")
        lines.append(f"  Local Runtime Summary: {get_runtime_summary_status(lab)}")
        lines.append(f"  Focus: {get_lab_focus(lab)}")
    lines.append("")

    lines.append("5. Artifact Coverage")
    lines.append(f"- Scenario metadata files: {count_files('scenarios/*/*/metadata.yaml')}")
    lines.append(f"- Scenario poster SVG files: {count_files('scenarios/**/*.svg')}")
    lines.append(f"- Scenario poster PNG files: {count_files('scenarios/**/*.png')}")
    lines.append(f"- Missing required artifacts: {values['missing_required_artifacts']}")
    lines.append(f"- Small PNG count: {values['small_png_count']}")
    lines.append("")

    lines.append("6. Validation Signals")
    lines.append(f"- Markdown broken links: {values['markdown_broken_links']}")
    lines.append(f"- Top-level missing directories: {values['top_level_missing_directories']}")
    lines.append(f"- Top-level extra directories: {values['top_level_extra_directories']}")
    lines.append(f"- Top-level missing README mentions: {values['top_level_missing_readme_mentions']}")
    lines.append(f"- Root README missing links: {values['root_readme_missing_links']}")
    lines.append(f"- Root README missing terms: {values['root_readme_missing_terms']}")
    lines.append(f"- Repository language hits: {values['repository_language_hits']}")
    lines.append(f"- Lab missing required paths: {values['lab_missing_required_paths']}")
    lines.append(f"- Lab missing required status terms: {values['lab_missing_status_terms']}")
    lines.append("")

    lines.append("7. Report Layering")
    lines.append("- docs/: stable reviewer-facing repository documentation")
    lines.append("- reports/: generated detailed checker outputs for maintainers")
    lines.append("- validation-reports/: reviewer-facing validation summaries")
    lines.append("- a.txt: local-only executive summary")
    lines.append("")

    lines.append("8. Reviewer Entry Points")
    for entry in [
        "README.md",
        "validation-reports/lab-readiness-summary.md",
        "docs/lab-coverage-matrix.md",
        "docs/repository-tree.md",
        "docs/report-layer-guide.md",
        "scenarios/README.md",
        "labs/*/README.md",
    ]:
        lines.append(f"- {entry}")
    lines.append("")

    lines.append("9. Current Baseline")
    lines.append(f"- {total_scenarios} lifecycle-aligned scenarios")
    lines.append(f"- {len(labs)} implementation labs")
    lines.append(f"- {count_files('labs/*/architecture/implementation-plan.md')} lab implementation plans")
    lines.append(f"- {count_files('labs/*/validation-reports/lab-validation-report.md')} lab validation reports")
    lines.append(f"- {count_files('labs/*/validation-reports/scenario-coverage-report.md')} scenario coverage reports")
    lines.append(f"- {count_files('labs/*/evidence/README.md')} lab evidence boundaries")
    lines.append(f"- {count_files('labs/*/scripts/README.md')} lab script boundaries")
    lines.append(f"- Repository validation target: {validation_status}")
    lines.append("")

    lines.append("10. Implementation Boundary")
    lines.append("- Current repository baseline remains documentation-ready")
    lines.append("- Runtime implementation is planned and incrementally starting from foundational labs")
    if execution_note_labs:
        lines.append("- Execution boundary has been documented for:")
        for lab_name in execution_note_labs:
            lines.append(f"  - {lab_name}")
    else:
        lines.append("- No execution boundary has been documented yet")
    lines.append("- Generated runtime evidence remains local-only unless explicitly promoted to reviewer-facing evidence")
    lines.append("")

    lines.append("11. Recommended Implementation Order")
    for item in IMPLEMENTATION_ORDER:
        status = "present" if (ROOT / "labs" / item).exists() else "missing"
        lines.append(f"- {item} | {status}")
    lines.append("")

    lines.append("12. Operational Summary")
    if validation_status == "PASS":
        lines.append("The repository currently presents a validation-clean documentation-ready portfolio baseline.")
    else:
        lines.append("The repository currently requires validation follow-up before being treated as a clean baseline.")
    lines.append("Scenarios define operational validation cases.")
    lines.append("Labs define implementation boundaries.")
    lines.append("Modules, adapters, and shared runtime areas define capability and integration boundaries.")
    lines.append("The next major phase is executable lab implementation, starting with Linux observability.")
    lines.append("")

    return "\n".join(lines)

def main():
    OUTPUT.write_text(build_summary(), encoding="utf-8")
    print("[OK] wrote a.txt")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())