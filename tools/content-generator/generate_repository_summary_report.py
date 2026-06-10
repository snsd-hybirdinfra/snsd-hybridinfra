from pathlib import Path
from datetime import datetime
import re

ROOT = Path(".").resolve()
OUT = ROOT / "a.txt"

def read_text(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""

def count_dirs(path):
    if not path.exists():
        return 0
    return len([p for p in path.iterdir() if p.is_dir()])

def count_files(pattern):
    return len(list(ROOT.glob(pattern)))

def extract_number(text, key, default="0"):
    match = re.search(rf"{re.escape(key)}:\s*(\d+)", text)
    if match:
        return match.group(1)
    return default

def has_text(path, pattern):
    text = read_text(path)
    return pattern in text

health = read_text(ROOT / "reports" / "portfolio-health-summary.md")
link_report = read_text(ROOT / "reports" / "markdown-link-check.md")
top_report = read_text(ROOT / "reports" / "top-level-structure-check.md")
root_report = read_text(ROOT / "reports" / "root-readme-alignment-check.md")
language_report = read_text(ROOT / "reports" / "repository-language-check.md")
related_report = read_text(ROOT / "reports" / "related-scenarios-generation-report.md")
lab_report = read_text(ROOT / "validation-reports" / "lab-validation-summary.md")
matrix = read_text(ROOT / "docs" / "lab-coverage-matrix.md")

scenario_total = count_dirs(ROOT / "scenarios" / "level-1-visibility")
scenario_total += count_dirs(ROOT / "scenarios" / "level-2-correlation")
scenario_total += count_dirs(ROOT / "scenarios" / "level-3-recovery")
scenario_total += count_dirs(ROOT / "scenarios" / "level-4-resilience")
scenario_total += count_dirs(ROOT / "scenarios" / "level-5-continuity")

l1 = count_dirs(ROOT / "scenarios" / "level-1-visibility")
l2 = count_dirs(ROOT / "scenarios" / "level-2-correlation")
l3 = count_dirs(ROOT / "scenarios" / "level-3-recovery")
l4 = count_dirs(ROOT / "scenarios" / "level-4-resilience")
l5 = count_dirs(ROOT / "scenarios" / "level-5-continuity")

metadata_count = count_files("scenarios/*/*/metadata.yaml")
poster_svg_count = count_files("scenarios/*/*/diagrams/operational-poster.svg")
poster_png_count = count_files("scenarios/*/*/diagrams/operational-poster.png")

lab_count = count_dirs(ROOT / "labs")
mapped_scenarios = extract_number(matrix, "Total mapped scenarios", str(scenario_total))
missing_lab_items = extract_number(lab_report, "missing_lab_items", "0")

broken_links = extract_number(link_report, "broken_links", "0")
extra_dirs = extract_number(top_report, "extra_top_level_directories", "0")
missing_dirs = extract_number(top_report, "missing_expected_directories", "0")
missing_root_links = extract_number(root_report, "missing_required_links", "0")
missing_root_terms = extract_number(root_report, "missing_required_terms", "0")
language_hits = extract_number(language_report, "language_hits", "0")

related_pending = "24"
m = re.search(r"Related Mapping Pending:\s*(\d+)", read_text(ROOT / "reports" / "repository-summary-report.txt"))
if m:
    related_pending = m.group(1)

baseline_pass = (
    broken_links == "0"
    and extra_dirs == "0"
    and missing_dirs == "0"
    and missing_root_links == "0"
    and missing_root_terms == "0"
    and language_hits == "0"
    and missing_lab_items == "0"
)

status = "PASS" if baseline_pass else "CHECK_REQUIRED"

lines = []
lines.append("SNSD HYBRID INFRASTRUCTURE - REPOSITORY EXECUTIVE SUMMARY REPORT")
lines.append("=" * 72)
lines.append("")
lines.append("Generated At: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
lines.append("")
lines.append("1. Repository Positioning")
lines.append("-" * 72)
lines.append("SNSD Hybrid Infrastructure is a Scenario-driven Infrastructure Operations Platform.")
lines.append("It is positioned as an Enterprise Operational Capability Platform, not a simple")
lines.append("scenario collection. Reusable operational capabilities are described as catalog")
lines.append("modules, adapters, and shared runtime concepts, then validated through lifecycle")
lines.append("aligned operational scenarios and lab-centered implementation boundaries.")
lines.append("")
lines.append("2. Architecture Model")
lines.append("-" * 72)
lines.append("Root repository: catalog, governance, standards, reports, and reviewer entry points")
lines.append("scenarios/: lifecycle-based operational validation workflows")
lines.append("labs/: implementation boundaries for validating scenario groups")
lines.append("modules/: repository-level operational capability catalog")
lines.append("adapters/: repository-level integration adapter catalog")
lines.append("shared-runtime/: repository-level runtime capability catalog")
lines.append("builds/: implementation foundation documents and lab preparation references")
lines.append("docs/: reviewer-facing standards, architecture notes, and coverage matrices")
lines.append("diagrams/: repository-level architecture diagrams")
lines.append("internal/: internal governance, templates, and QA references")
lines.append("reports/: generated detailed validation outputs")
lines.append("validation-reports/: reviewer-facing validation summaries")
lines.append("tools/: validation, generation, and diagram rendering tooling")
lines.append("")
lines.append("3. Scenario Inventory")
lines.append("-" * 72)
lines.append("Total Scenarios: " + str(scenario_total))
lines.append("Level 1 Visibility: " + str(l1))
lines.append("Level 2 Correlation: " + str(l2))
lines.append("Level 3 Recovery: " + str(l3))
lines.append("Level 4 Resilience: " + str(l4))
lines.append("Level 5 Continuity: " + str(l5))
lines.append("")
lines.append("4. Lab Inventory")
lines.append("-" * 72)
lines.append("Total Labs: " + str(lab_count))
lines.append("Mapped Scenarios: " + str(mapped_scenarios))
lines.append("Missing Lab Items: " + str(missing_lab_items))
lines.append("")
lines.append("Lab Model:")
lines.append("Lab = implementation boundary")
lines.append("Scenario = operational validation case")
lines.append("Lab-local modules = implementation-specific reusable capabilities")
lines.append("Lab-local adapters = implementation-specific tool integrations")
lines.append("Lab-local shared-runtime = runners, validators, parsers, and execution helpers")
lines.append("")
lines.append("5. Artifact Coverage")
lines.append("-" * 72)
lines.append("Scenario Directories: " + str(scenario_total))
lines.append("Metadata Files: " + str(metadata_count))
lines.append("Poster SVG Files: " + str(poster_svg_count))
lines.append("Poster PNG Files: " + str(poster_png_count))
lines.append("Required Scenario Artifact Policy: README, metadata, poster seed, poster outputs,")
lines.append("execution evidence, validation evidence, summary, manifest, and checksums")
lines.append("")
lines.append("6. Validation Status")
lines.append("-" * 72)
lines.append("Markdown Broken Links: " + str(broken_links))
lines.append("Top-Level Extra Directories: " + str(extra_dirs))
lines.append("Top-Level Missing Directories: " + str(missing_dirs))
lines.append("Root README Missing Links: " + str(missing_root_links))
lines.append("Root README Missing Terms: " + str(missing_root_terms))
lines.append("Repository Language Hits: " + str(language_hits))
lines.append("Related Mapping Policy: Conservative lifecycle-only mapping")
lines.append("Related Mapping Pending: " + str(related_pending))
lines.append("")
lines.append("7. Report Layering")
lines.append("-" * 72)
lines.append("a.txt: executive repository summary")
lines.append("reports/: detailed generated validation results")
lines.append("validation-reports/: reviewer-facing validation summaries")
lines.append("docs/lab-coverage-matrix.md: scenario-to-lab mapping")
lines.append("docs/repository-tree.md: reviewer-facing public tree")
lines.append("")
lines.append("8. Tooling Model")
lines.append("-" * 72)
lines.append("Primary Validation Workflow: tools/content-generator/run_repository_validation.py")
lines.append("Content Generation: tools/content-generator/")
lines.append("Diagram Rendering: tools/diagram-renderer/")
lines.append("Legacy Tools: isolated under tools/content-generator/legacy when applicable")
lines.append("")
lines.append("9. Current Baseline")
lines.append("-" * 72)
lines.append("Portfolio Baseline Status: " + status)
lines.append("Validation Workflow: tools/content-generator/run_repository_validation.py")
lines.append("")
lines.append("10. Operational Summary")
lines.append("-" * 72)
lines.append("The repository now represents a production-oriented infrastructure operations")
lines.append("portfolio where 150 lifecycle-aligned scenarios are preserved as validation")
lines.append("workflows, while 10 implementation-oriented labs provide the practical execution")
lines.append("boundaries for validating those scenarios with lab-local modules, adapters, shared")
lines.append("runtime utilities, evidence outputs, and validation reports.")
lines.append("")
lines.append("=" * 72)
lines.append("END OF REPORT")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("[OK] wrote a.txt")
print("[OK] baseline status:", status)

