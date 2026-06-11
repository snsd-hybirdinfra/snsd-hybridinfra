from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
REPORT = ROOT / "reports" / "root-readme-alignment-check.md"

REQUIRED_LINKS = [
    "scenarios/",
    "labs/",
    "modules/",
    "adapters/",
    "shared-runtime/",
    "docs/",
    "reports/",
    "validation-reports/",
]

REQUIRED_TERMS = [
    "SNSD Hybrid Infrastructure",
    "Scenario-driven Infrastructure Operations Platform",
    "Enterprise Operational Capability Platform",
    "Detection",
    "Correlation",
    "Incident Coordination",
    "Recovery",
    "Validation",
    "Governance",
]

REQUIRED_MARKERS = [
    "SCENARIO_INVENTORY_START",
    "SCENARIO_INVENTORY_END",
    "QUALITY_STATUS_START",
    "QUALITY_STATUS_END",
]

def contains_case_insensitive(text: str, value: str) -> bool:
    return value.lower() in text.lower()

def main() -> int:
    if not README.exists():
        print("[FAIL] README.md not found")
        return 1

    text = README.read_text(encoding="utf-8-sig", errors="replace")

    missing_links = [
        item for item in REQUIRED_LINKS
        if item not in text
    ]

    missing_terms = [
        item for item in REQUIRED_TERMS
        if not contains_case_insensitive(text, item)
    ]

    missing_markers = [
        item for item in REQUIRED_MARKERS
        if item not in text
    ]

    REPORT.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Root README Alignment Check")
    lines.append("")
    lines.append("| Check | Count |")
    lines.append("|---|---:|")
    lines.append(f"| root_readme_missing_links | {len(missing_links)} |")
    lines.append(f"| root_readme_missing_terms | {len(missing_terms)} |")
    lines.append(f"| root_readme_missing_markers | {len(missing_markers)} |")
    lines.append("")
    lines.append("## Missing Links")
    lines.append("")
    if missing_links:
        for item in missing_links:
            lines.append(f"- {item}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Missing Terms")
    lines.append("")
    if missing_terms:
        for item in missing_terms:
            lines.append(f"- {item}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Missing Markers")
    lines.append("")
    if missing_markers:
        for item in missing_markers:
            lines.append(f"- {item}")
    else:
        lines.append("- None")
    lines.append("")

    REPORT.write_text("\n".join(lines), encoding="utf-8")

    if missing_links or missing_terms or missing_markers:
        print("[FAIL] Root README alignment check failed")
        print(f"missing_links={len(missing_links)}")
        print(f"missing_terms={len(missing_terms)}")
        print(f"missing_markers={len(missing_markers)}")
        return 1

    print("[OK] Root README alignment check passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())