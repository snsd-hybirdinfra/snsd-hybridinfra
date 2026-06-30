#!/usr/bin/env python3
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[2]
SCENARIOS_DIR = REPO_ROOT / "scenarios"
OUTPUT = REPO_ROOT / "docs" / "lab-runtime-validation-index.md"

LEVEL_ORDER = [
    "level-1-visibility",
    "level-2-correlation",
    "level-3-recovery",
    "level-4-distributed-resilience",
    "level-5-enterprise-continuity",
]

LEVEL_LABELS = {
    "level-1-visibility": "Level 1 - Visibility",
    "level-2-correlation": "Level 2 - Correlation",
    "level-3-recovery": "Level 3 - Recovery",
    "level-4-distributed-resilience": "Level 4 - Distributed Resilience",
    "level-5-enterprise-continuity": "Level 5 - Enterprise Continuity",
}

def evidence_path_for(scenario_dir: Path) -> Path:
    return scenario_dir / "evidence" / "generated" / "lab-runtime-validation.md"

def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")

def status_for(evidence_path: Path) -> str:
    if not evidence_path.exists():
        return "MISSING"
    text = read_text(evidence_path)
    if "NOT_FOUND:" in text:
        return "NOT_FOUND"
    return "OK"

def scenario_rows():
    rows = []
    for level_dir in sorted(SCENARIOS_DIR.glob("level-*")):
        if not level_dir.is_dir():
            continue
        for scenario_dir in sorted(level_dir.iterdir()):
            if not scenario_dir.is_dir():
                continue
            evidence_path = evidence_path_for(scenario_dir)
            status = status_for(evidence_path)
            rel_evidence = evidence_path.relative_to(REPO_ROOT).as_posix()
            rows.append({
                "level": level_dir.name,
                "scenario": scenario_dir.name,
                "status": status,
                "evidence": rel_evidence,
            })
    return rows

def main():
    rows = scenario_rows()

    status_counter = Counter(row["status"] for row in rows)
    level_counter = Counter(row["level"] for row in rows)
    level_status_counter = defaultdict(Counter)

    for row in rows:
        level_status_counter[row["level"]][row["status"]] += 1

    total = len(rows)
    ok = status_counter.get("OK", 0)
    missing = status_counter.get("MISSING", 0)
    not_found = status_counter.get("NOT_FOUND", 0)

    lines = []
    lines.append("# Lab Runtime Validation Index")
    lines.append("")
    lines.append(f"Generated At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("This document indexes reviewer-facing runtime validation evidence generated for scenario packages.")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"- Total scenarios: {total}")
    lines.append(f"- OK: {ok}")
    lines.append(f"- Missing evidence: {missing}")
    lines.append(f"- Contains NOT_FOUND: {not_found}")
    lines.append("")
    lines.append("## Reviewer Interpretation")
    lines.append("")
    lines.append("- `OK` means the scenario has generated reviewer-facing runtime validation evidence.")
    lines.append("- `MISSING` means the scenario evidence file does not exist.")
    lines.append("- `NOT_FOUND` means the evidence file exists but references missing local runtime evidence.")
    lines.append("")
    lines.append("Reviewer-facing evidence is stored under each scenario directory:")
    lines.append("")
    lines.append("    scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md")
    lines.append("")
    lines.append("Local raw runtime evidence is generated under:")
    lines.append("")
    lines.append("    labs/evidence/generated/")
    lines.append("")
    lines.append("## Level Summary")
    lines.append("")
    lines.append("| Level | Total | OK | Missing | NOT_FOUND |")
    lines.append("|---|---:|---:|---:|---:|")

    for level in LEVEL_ORDER:
        total_level = level_counter.get(level, 0)
        ok_level = level_status_counter[level].get("OK", 0)
        missing_level = level_status_counter[level].get("MISSING", 0)
        not_found_level = level_status_counter[level].get("NOT_FOUND", 0)
        label = LEVEL_LABELS.get(level, level)
        lines.append(f"| {label} | {total_level} | {ok_level} | {missing_level} | {not_found_level} |")

    extra_levels = sorted(set(level_counter) - set(LEVEL_ORDER))
    for level in extra_levels:
        total_level = level_counter.get(level, 0)
        ok_level = level_status_counter[level].get("OK", 0)
        missing_level = level_status_counter[level].get("MISSING", 0)
        not_found_level = level_status_counter[level].get("NOT_FOUND", 0)
        lines.append(f"| {level} | {total_level} | {ok_level} | {missing_level} | {not_found_level} |")

    lines.append("")
    lines.append("## Review Path")
    lines.append("")
    lines.append("Recommended review order:")
    lines.append("")
    lines.append("1. Check the Executive Summary.")
    lines.append("2. Confirm all levels show `Missing = 0` and `NOT_FOUND = 0`.")
    lines.append("3. Open representative scenario evidence files from Level 1, Level 3, Level 4, and Level 5.")
    lines.append("4. Review `docs/failure-injection-scenarios.md` for controlled failure validation.")
    lines.append("5. Review `docs/runtime-validation-pipeline.md` for evidence generation workflow.")
    lines.append("")
    lines.append("## Scenario Evidence Index")
    lines.append("")

    for level in LEVEL_ORDER + extra_levels:
        level_rows = [row for row in rows if row["level"] == level]
        if not level_rows:
            continue

        label = LEVEL_LABELS.get(level, level)
        lines.append(f"### {label}")
        lines.append("")
        lines.append("| Scenario | Status | Evidence |")
        lines.append("|---|---|---|")

        for row in level_rows:
            lines.append(
                f"| `{row['scenario']}` | {row['status']} | `{row['evidence']}` |"
            )

        lines.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"[OK] generated {OUTPUT.relative_to(REPO_ROOT)}")
    print(f"[OK] total={total} ok={ok} missing={missing} not_found={not_found}")

if __name__ == "__main__":
    main()
