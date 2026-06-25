from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[2]
SCENARIOS_ROOT = REPO_ROOT / "scenarios"
OUTPUT_PATH = REPO_ROOT / "docs" / "scenario-test-evidence-index.md"

LAB_PATTERN = re.compile(r"(01|02|03|04|05|06|07|08|09|10)-[a-z0-9-]+-lab")

LEVEL_NAMES = {
    "level-1-visibility": "Level 1 Visibility",
    "level-2-correlation": "Level 2 Correlation",
    "level-3-recovery": "Level 3 Recovery",
    "level-4-resilience": "Level 4 Resilience",
    "level-5-continuity": "Level 5 Continuity",
}

def extract_mapped_lab(evidence_file: Path) -> str:
    if not evidence_file.exists():
        return "MISSING"

    text = evidence_file.read_text(encoding="utf-8", errors="ignore")

    for line in text.splitlines():
        if "Mapped Lab" in line or "mapped lab" in line:
            match = LAB_PATTERN.search(line)
            if match:
                return match.group(0)

    match = LAB_PATTERN.search(text)
    if match:
        return match.group(0)

    return "MISSING"

def has_study_evidence(scenario_dir: Path) -> str:
    path = scenario_dir / "evidence" / "generated" / "lab-based-study-validation.md"
    return "YES" if path.exists() else "NO"

def scenario_status(scenario_dir: Path, lab: str) -> str:
    if lab == "MISSING":
        return "MISSING_MAPPING"

    test_file = scenario_dir / "evidence" / "generated" / "scenario-test-evidence.md"
    result_file = scenario_dir / "evidence" / "generated" / "scenario-validation-result.md"
    matrix_file = scenario_dir / "evidence" / "generated" / "scenario-evidence-matrix.tsv"
    study_file = scenario_dir / "evidence" / "generated" / "lab-based-study-validation.md"

    required = [test_file, result_file, matrix_file]

    if not all(path.exists() for path in required):
        return "PARTIAL_EVIDENCE"

    if study_file.exists():
        return "STUDY_VALIDATED"

    return "EVIDENCE_READY"

def collect_rows() -> list[dict[str, str]]:
    rows = []

    for level_dir in sorted(SCENARIOS_ROOT.glob("level-*")):
        if not level_dir.is_dir():
            continue

        level_key = level_dir.name
        level_name = LEVEL_NAMES.get(level_key, level_key)

        for scenario_dir in sorted(level_dir.iterdir()):
            if not scenario_dir.is_dir():
                continue

            scenario = scenario_dir.name
            evidence_file = scenario_dir / "evidence" / "generated" / "scenario-test-evidence.md"
            lab = extract_mapped_lab(evidence_file)
            study = has_study_evidence(scenario_dir)
            status = scenario_status(scenario_dir, lab)

            rows.append({
                "level_key": level_key,
                "level_name": level_name,
                "scenario": scenario,
                "mapped_lab": lab,
                "study_evidence": study,
                "status": status,
                "evidence_path": str(evidence_file.relative_to(REPO_ROOT)).replace("\\", "/"),
            })

    return rows

def render(rows: list[dict[str, str]]) -> str:
    total = len(rows)
    level_counts = Counter(row["level_name"] for row in rows)
    lab_counts = Counter(row["mapped_lab"] for row in rows)
    status_counts = Counter(row["status"] for row in rows)
    study_count = sum(1 for row in rows if row["study_evidence"] == "YES")

    lines = []

    lines.append("# Scenario Test Evidence Index")
    lines.append("")
    lines.append("This document indexes scenario-level test evidence and mapped lab relationships across the SNSD Hybrid Infrastructure repository.")
    lines.append("")
    lines.append("The index is generated from each scenario evidence file under:")
    lines.append("")
    lines.append("scenarios/<level>/<scenario>/evidence/generated/scenario-test-evidence.md")
    lines.append("")
    lines.append("Lab-based study validation files are checked under:")
    lines.append("")
    lines.append("scenarios/<level>/<scenario>/evidence/generated/lab-based-study-validation.md")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Total scenarios | {total} |")
    lines.append(f"| Scenarios with lab-based study evidence | {study_count} |")
    lines.append(f"| Labs referenced | {len([lab for lab in lab_counts if lab != 'MISSING'])} |")
    lines.append("")

    lines.append("## Scenario Count by Level")
    lines.append("")
    lines.append("| Level | Scenario Count |")
    lines.append("|---|---:|")
    for level_name in sorted(level_counts):
        lines.append(f"| {level_name} | {level_counts[level_name]} |")
    lines.append("")

    lines.append("## Scenario Count by Mapped Lab")
    lines.append("")
    lines.append("| Mapped Lab | Scenario Count |")
    lines.append("|---|---:|")
    for lab, count in sorted(lab_counts.items()):
        lines.append(f"| {lab} | {count} |")
    lines.append("")

    lines.append("## Evidence Status Summary")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for status, count in sorted(status_counts.items()):
        lines.append(f"| {status} | {count} |")
    lines.append("")

    rows_by_level = defaultdict(list)
    for row in rows:
        rows_by_level[row["level_name"]].append(row)

    for level_name in sorted(rows_by_level):
        lines.append(f"## {level_name}")
        lines.append("")
        lines.append("| Scenario | Mapped Lab | Study Evidence | Status | Evidence Path |")
        lines.append("|---|---|---|---|---|")

        for row in sorted(rows_by_level[level_name], key=lambda item: item["scenario"]):
            lines.append(
                f"| {row['scenario']} | {row['mapped_lab']} | {row['study_evidence']} | {row['status']} | {row['evidence_path']} |"
            )

        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- Mapped Lab is extracted from scenario-test-evidence.md.")
    lines.append("- Study Evidence indicates whether lab-based-study-validation.md exists for the scenario.")
    lines.append("- STUDY_VALIDATED means the scenario has baseline generated evidence and lab-based study evidence.")
    lines.append("- EVIDENCE_READY means baseline scenario evidence exists but lab-based study evidence has not been generated yet.")
    lines.append("- PARTIAL_EVIDENCE means at least one expected baseline evidence file is missing.")
    lines.append("- MISSING_MAPPING means no mapped lab could be extracted.")
    lines.append("")

    return "\n".join(lines)

def main() -> int:
    rows = collect_rows()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render(rows), encoding="utf-8")

    print(f"[OK] wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"[OK] total scenarios: {len(rows)}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
