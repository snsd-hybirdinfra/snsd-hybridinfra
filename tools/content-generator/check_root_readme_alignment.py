from pathlib import Path
import sys

ROOT = Path(".").resolve()
README = ROOT / "README.md"
REPORT = ROOT / "reports" / "root-readme-alignment-check.md"

required_patterns = [
    ("Scenario Inventory", "./scenarios/README.md"),
    ("Operational Modules", "./modules/README.md"),
    ("Operational Adapters", "./adapters/README.md"),
    ("Shared Runtime", "./shared-runtime/README.md"),
    ("Build Foundations", "./builds/README.md"),
    ("Reports", "./reports/README.md"),
    ("Tools", "./tools/README.md"),
    ("Documentation", "./docs/README.md"),
    ("Portfolio Health Summary", "./reports/portfolio-health-summary.md"),
    ("Repository Quality Check", "./reports/repository-quality-check.md"),
    ("Markdown Link Check", "./reports/markdown-link-check.md"),
    ("Top-Level Structure Check", "./reports/top-level-structure-check.md"),
    ("Related Scenarios Generation Report", "./reports/related-scenarios-generation-report.md"),
]

required_terms = [
    "Enterprise Operational Capability Platform",
    "scenario-driven infrastructure operations portfolio",
    "Detection",
    "Correlation & Analysis",
    "Incident Coordination",
    "Recovery & Automation",
    "Recovery Validation",
    "Governance & Reporting",
    "Total scenarios: 123",
    "tools/content-generator/",
    "tools/diagram-renderer/",
]

text = README.read_text(encoding="utf-8-sig", errors="replace") if README.exists() else ""

missing_links = []
for label, path in required_patterns:
    if label not in text or path not in text:
        missing_links.append(f"{label} -> {path}")

missing_terms = []
for term in required_terms:
    if term not in text:
        missing_terms.append(term)

lines = []
lines.append("# Root README Alignment Check")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("```text")
lines.append(f"required_links: {len(required_patterns)}")
lines.append(f"missing_required_links: {len(missing_links)}")
lines.append(f"required_terms: {len(required_terms)}")
lines.append(f"missing_required_terms: {len(missing_terms)}")
lines.append("```")
lines.append("")
lines.append("## Missing Required Links")
lines.append("")
lines.append("```text")
lines.extend(missing_links if missing_links else ["NONE"])
lines.append("```")
lines.append("")
lines.append("## Missing Required Terms")
lines.append("")
lines.append("```text")
lines.extend(missing_terms if missing_terms else ["NONE"])
lines.append("```")

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"[OK] wrote {REPORT}")
print(f"[OK] missing required links: {len(missing_links)}")
print(f"[OK] missing required terms: {len(missing_terms)}")

if missing_links or missing_terms:
    sys.exit(1)
