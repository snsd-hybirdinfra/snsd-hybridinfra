#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[2]
SCENARIOS_DIR = ROOT / "scenarios"
OUTPUT = ROOT / "docs" / "lab-runtime-validation-index.md"

def extract_related_labs(text: str) -> list[str]:
    labs = []
    in_section = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped == "## Related Runtime Labs":
            in_section = True
            continue

        if in_section and stripped.startswith("## "):
            break

        if in_section and stripped.startswith("- `") and stripped.endswith("`"):
            labs.append(stripped.replace("- `", "").replace("`", ""))

    return labs

def main() -> int:
    scenario_dirs = sorted(
        p for p in SCENARIOS_DIR.glob("level-*/*")
        if p.is_dir()
    )

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    rows = []
    level_counter = Counter()
    status_counter = Counter()
    lab_counter = Counter()
    missing = []
    not_found = []

    for scenario_dir in scenario_dirs:
        level = scenario_dir.parent.name
        scenario = scenario_dir.name
        evidence_file = scenario_dir / "evidence" / "generated" / "lab-runtime-validation.md"

        level_counter[level] += 1

        if not evidence_file.exists():
            status = "missing"
            labs = []
            missing.append(str(evidence_file.relative_to(ROOT)))
        else:
            text = evidence_file.read_text(encoding="utf-8", errors="replace")
            has_not_found = "NOT_FOUND:" in text
            labs = extract_related_labs(text)

            if has_not_found:
                status = "contains-not-found"
                not_found.append(str(evidence_file.relative_to(ROOT)))
            else:
                status = "ok"

            for lab in labs:
                lab_counter[lab] += 1

        status_counter[status] += 1
        rows.append((level, scenario, status, labs, evidence_file.relative_to(ROOT)))

    lines = []
    lines.append("# Lab Runtime Validation Index")
    lines.append("")
    lines.append(f"Generated At: {generated_at}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total scenarios: {len(scenario_dirs)}")
    lines.append(f"- OK: {status_counter.get('ok', 0)}")
    lines.append(f"- Missing evidence: {status_counter.get('missing', 0)}")
    lines.append(f"- Contains NOT_FOUND: {status_counter.get('contains-not-found', 0)}")
    lines.append("")
    lines.append("## Level Coverage")
    lines.append("")
    lines.append("| Level | Scenario Count |")
    lines.append("|---|---:|")
    for level, count in sorted(level_counter.items()):
        lines.append(f"| `{level}` | {count} |")
    lines.append("")
    lines.append("## Runtime Lab Usage")
    lines.append("")
    lines.append("| Runtime Lab | Linked Scenario Count |")
    lines.append("|---|---:|")
    for lab, count in sorted(lab_counter.items()):
        lines.append(f"| `{lab}` | {count} |")
    lines.append("")
    lines.append("## Scenario Runtime Evidence Status")
    lines.append("")
    lines.append("| Level | Scenario | Status | Related Runtime Labs | Evidence File |")
    lines.append("|---|---|---|---|---|")

    for level, scenario, status, labs, evidence_path in rows:
        lab_text = ", ".join(f"`{lab}`" for lab in labs) if labs else "-"
        lines.append(
            f"| `{level}` | `{scenario}` | `{status}` | {lab_text} | `{evidence_path}` |"
        )

    if missing:
        lines.append("")
        lines.append("## Missing Evidence Files")
        lines.append("")
        for item in missing:
            lines.append(f"- `{item}`")

    if not_found:
        lines.append("")
        lines.append("## Evidence Files Containing NOT_FOUND")
        lines.append("")
        for item in not_found:
            lines.append(f"- `{item}`")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] wrote {OUTPUT.relative_to(ROOT)}")
    print(f"[OK] total={len(scenario_dirs)} ok={status_counter.get('ok', 0)} missing={status_counter.get('missing', 0)} not_found={status_counter.get('contains-not-found', 0)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
