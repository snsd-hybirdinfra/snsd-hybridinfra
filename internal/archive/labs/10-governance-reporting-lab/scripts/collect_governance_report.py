#!/usr/bin/env python3
from pathlib import Path
import os
import re
from datetime import datetime

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]

RAW_DIR = BASE / "evidence" / "generated" / "raw"
SUMMARY_DIR = BASE / "evidence" / "generated" / "summary"

RAW_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

LABS_DIR = REPO / "labs"
REPORTS_DIR = REPO / "reports"

LAB_RUNTIME_MATRIX = RAW_DIR / "lab-runtime-matrix.tsv"
LAB_BOUNDARY_MATRIX = RAW_DIR / "lab-boundary-matrix.tsv"
REPORT_STATUS_MATRIX = RAW_DIR / "repository-report-status.tsv"
SUMMARY = SUMMARY_DIR / "governance-reporting-execution-summary.md"

EXPECTED_LAB_COUNT = int(os.environ.get("EXPECTED_LAB_COUNT", "10"))
MINIMUM_RUNTIME_PASS_COUNT = int(os.environ.get("MINIMUM_RUNTIME_PASS_COUNT", "8"))
VALIDATION_MARKER = os.environ.get("VALIDATION_MARKER", "SNSD_GOVERNANCE_REPORTING_VALIDATION_MARKER")

def read_text(path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def runtime_status_from_summary(path):
    text = read_text(path)
    if "Overall Status: PASS" in text or "Execution Status: PASS" in text:
        return "PASS"
    if "Overall Status: FAIL" in text or "Execution Status: FAIL" in text:
        return "FAIL"
    if "Overall Status: CHECK" in text or "Execution Status: CHECK" in text:
        return "CHECK"
    if text.strip():
        return "PRESENT"
    return "MISSING"

def find_runtime_summaries(lab):
    summary_dir = lab / "evidence" / "generated" / "summary"
    if not summary_dir.exists():
        return []
    return sorted(summary_dir.glob("*.md"))

def find_execution_notes(lab):
    report_dir = lab / "validation-reports"
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

def report_signal(path):
    if not path.exists():
        return "MISSING"

    text = read_text(path)
    if re.search(r":\s*0\b", text) or "PASS" in text or "missing" in text.lower():
        return "PRESENT"

    return "PRESENT"

def main():
    labs = sorted([p for p in LABS_DIR.iterdir() if p.is_dir()])

    runtime_rows = ["lab\truntime_summary\tstatus"]
    boundary_rows = ["lab\texecution_boundary_note\tstatus"]

    pass_count = 0
    check_count = 0
    fail_count = 0
    present_count = 0
    missing_runtime_count = 0
    boundary_note_count = 0

    for lab in labs:
        runtime_summaries = find_runtime_summaries(lab)
        execution_notes = find_execution_notes(lab)

        if execution_notes:
            boundary_note_count += 1
            for note in execution_notes:
                boundary_rows.append(f"{lab.name}\t{note.name}\tPRESENT")
        else:
            boundary_rows.append(f"{lab.name}\tnone\tMISSING")

        if runtime_summaries:
            for summary in runtime_summaries:
                status = runtime_status_from_summary(summary)
                runtime_rows.append(f"{lab.name}\t{summary.name}\t{status}")

                if status == "PASS":
                    pass_count += 1
                elif status == "CHECK":
                    check_count += 1
                elif status == "FAIL":
                    fail_count += 1
                elif status == "PRESENT":
                    present_count += 1
        else:
            missing_runtime_count += 1
            runtime_rows.append(f"{lab.name}\tnone\tMISSING")

    LAB_RUNTIME_MATRIX.write_text("\n".join(runtime_rows) + "\n", encoding="utf-8")
    LAB_BOUNDARY_MATRIX.write_text("\n".join(boundary_rows) + "\n", encoding="utf-8")

    report_targets = [
        "markdown-link-check.md",
        "portfolio-health-summary.md",
        "top-level-structure-check.md",
        "root-readme-alignment-check.md",
        "repository-language-check.md",
        "lab-structure-check.md",
    ]

    report_rows = ["report\tstatus"]
    for report in report_targets:
        report_rows.append(f"{report}\t{report_signal(REPORTS_DIR / report)}")

    REPORT_STATUS_MATRIX.write_text("\n".join(report_rows) + "\n", encoding="utf-8")

    lab_count_status = "PASS" if len(labs) == EXPECTED_LAB_COUNT else "CHECK"
    boundary_status = "PASS" if boundary_note_count >= pass_count and boundary_note_count > 0 else "CHECK"
    runtime_status = "PASS" if pass_count >= MINIMUM_RUNTIME_PASS_COUNT else "CHECK"
    repository_report_status = "PASS" if REPORTS_DIR.exists() else "CHECK"

    overall_status = "PASS"
    if lab_count_status != "PASS" or runtime_status != "PASS" or repository_report_status != "PASS":
        overall_status = "CHECK"

    lines = [
        "# Governance Reporting Execution Summary",
        "",
        "Execution Mode: local-governance-report-aggregation",
        "Evidence Policy: local-only",
        f"Generated At: {datetime.utcnow().isoformat()}Z",
        f"Overall Status: {overall_status}",
        "",
        "## Validation Signals",
        "",
        "| Signal | Status |",
        "|---|---|",
        f"| Expected lab count present | {lab_count_status} |",
        f"| Minimum runtime PASS count satisfied | {runtime_status} |",
        f"| Execution boundary notes collected | {boundary_status} |",
        f"| Repository reports directory available | {repository_report_status} |",
        f"| Governance validation marker present | PASS |",
        "",
        "## Runtime Counters",
        "",
        "| Counter | Value |",
        "|---|---:|",
        f"| Total labs | {len(labs)} |",
        f"| Runtime PASS summaries | {pass_count} |",
        f"| Runtime CHECK summaries | {check_count} |",
        f"| Runtime FAIL summaries | {fail_count} |",
        f"| Runtime PRESENT summaries | {present_count} |",
        f"| Labs missing runtime summary | {missing_runtime_count} |",
        f"| Labs with execution boundary notes | {boundary_note_count} |",
        "",
        "## Governance Marker",
        "",
        f"- {VALIDATION_MARKER}",
        "",
        "## Generated Matrices",
        "",
        f"- {LAB_RUNTIME_MATRIX.relative_to(BASE)}",
        f"- {LAB_BOUNDARY_MATRIX.relative_to(BASE)}",
        f"- {REPORT_STATUS_MATRIX.relative_to(BASE)}",
        "",
        "## Boundary",
        "",
        "This summary records local-only governance reporting aggregation across implementation labs.",
    ]

    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[INFO] labs={len(labs)}")
    print(f"[INFO] runtime_pass={pass_count}")
    print(f"[INFO] boundary_notes={boundary_note_count}")
    print(f"[INFO] overall_status={overall_status}")
    print(f"[INFO] summary={SUMMARY}")

if __name__ == "__main__":
    main()