from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "reports" / "repository-optimization-audit.md"

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "runtime-workspace",
    "tmp",
    "temp",
    "debug",
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".py",
    ".sh",
    ".ps1",
    ".ini",
    ".cfg",
    ".conf",
    ".tsv",
    ".csv",
}

BINARY_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".svg",
    ".pdf",
    ".zip",
}


def is_ignored_path(path: Path) -> bool:
    parts = set(path.parts)
    return any(part in IGNORE_DIRS for part in parts)


def iter_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if is_ignored_path(path.relative_to(ROOT)):
            continue
        files.append(path)
    return sorted(files)


def file_sha(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_size(path: Path) -> int:
    return path.stat().st_size


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ""


def group_duplicate_hashes(files: list[Path]) -> dict[str, list[Path]]:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        groups[file_sha(path)].append(path)
    return {sha: paths for sha, paths in groups.items() if len(paths) > 1}


def find_large_files(files: list[Path], limit_bytes: int = 512 * 1024) -> list[Path]:
    return [path for path in files if file_size(path) >= limit_bytes]


def find_quality_status_anomalies() -> list[str]:
    readme = ROOT / "README.md"
    text = read_text(readme)
    findings = []

    if "| root_readme_missing_links | | root_readme_missing_links |" in text:
        findings.append("README.md quality status row for root_readme_missing_links is malformed")

    if "| root_readme_missing_terms | | root_readme_missing_terms |" in text:
        findings.append("README.md quality status row for root_readme_missing_terms is malformed")

    if "Phase 5 Scenario Evidence Report" not in text:
        findings.append("README.md does not expose Phase 5 Scenario Evidence Report in reviewer quick start")

    if "Scenario Test Evidence Index" not in text:
        findings.append("README.md does not expose Scenario Test Evidence Index in reviewer quick start")

    return findings


def find_status_language_anomalies() -> list[str]:
    findings = []

    labs_readme = ROOT / "labs" / "README.md"
    text = read_text(labs_readme)
    if "Total implementation labs | 10" in text and "documentation-ready" in text:
        findings.append("labs/README.md still emphasizes documentation-ready status while root README reports runtime PASS")

    summary_generator = ROOT / "tools" / "content-generator" / "generate_repository_summary_report.py"
    generator_text = read_text(summary_generator)
    if "documentation-ready portfolio baseline" in generator_text:
        findings.append("generate_repository_summary_report.py still contains old documentation-ready baseline wording")

    return findings


def find_domain_fragmentation() -> list[str]:
    scenarios_readme = ROOT / "scenarios" / "README.md"
    text = read_text(scenarios_readme)

    domain_lines = []
    in_domain_table = False
    for line in text.splitlines():
        if line.strip() == "## Domain Coverage":
            in_domain_table = True
            continue
        if in_domain_table and line.startswith("---"):
            break
        if in_domain_table and line.startswith("|") and not line.startswith("|---"):
            domain_lines.append(line)

    domains = []
    for line in domain_lines:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] != "Domain":
            domains.append(cells[0])

    groups = defaultdict(list)
    for domain in domains:
        prefix = domain.split("/")[0].strip()
        groups[prefix].append(domain)

    findings = []
    for prefix, values in sorted(groups.items()):
        if len(values) >= 3:
            findings.append(f"{prefix}: {', '.join(values)}")

    return findings


def find_scenario_evidence_counts() -> dict[str, int]:
    base = ROOT / "scenarios"
    return {
        "scenario-test-evidence.md": len(list(base.rglob("scenario-test-evidence.md"))),
        "scenario-evidence-matrix.tsv": len(list(base.rglob("scenario-evidence-matrix.tsv"))),
        "scenario-validation-result.md": len(list(base.rglob("scenario-validation-result.md"))),
    }


def find_candidate_generated_duplicates(files: list[Path]) -> list[Path]:
    candidates = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if "/evidence/generated/" in rel and path.name in {
            "scenario-test-evidence.md",
            "scenario-evidence-matrix.tsv",
            "scenario-validation-result.md",
        }:
            continue
        if path.name.lower() in {
            "execution-summary.md",
            "runtime-summary.md",
            "validation-result.md",
        }:
            candidates.append(path)
    return candidates


def main() -> int:
    files = iter_files()
    duplicate_hashes = group_duplicate_hashes(files)
    large_files = find_large_files(files)
    quality_findings = find_quality_status_anomalies()
    status_findings = find_status_language_anomalies()
    domain_findings = find_domain_fragmentation()
    evidence_counts = find_scenario_evidence_counts()
    generated_duplicate_candidates = find_candidate_generated_duplicates(files)

    lines = []
    lines.append("# Repository Optimization Audit")
    lines.append("")
    lines.append("## 1. Purpose")
    lines.append("")
    lines.append("This report identifies optimization and deduplication candidates before any destructive cleanup is performed.")
    lines.append("")
    lines.append("## 2. Summary")
    lines.append("")
    lines.append("| Signal | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Files scanned | {len(files)} |")
    lines.append(f"| Duplicate hash groups | {len(duplicate_hashes)} |")
    lines.append(f"| Large files over 512 KiB | {len(large_files)} |")
    lines.append(f"| README quality anomalies | {len(quality_findings)} |")
    lines.append(f"| Status language anomalies | {len(status_findings)} |")
    lines.append(f"| Domain fragmentation groups | {len(domain_findings)} |")
    lines.append("")
    lines.append("## 3. Scenario Evidence Artifact Counts")
    lines.append("")
    lines.append("| Artifact | Count | Expected | Status |")
    lines.append("|---|---:|---:|---|")
    for name, count in evidence_counts.items():
        lines.append(f"| {name} | {count} | 150 | {'PASS' if count == 150 else 'CHECK'} |")
    lines.append("")
    lines.append("## 4. README Quality Findings")
    lines.append("")
    if quality_findings:
        for item in quality_findings:
            lines.append(f"- CHECK: {item}")
    else:
        lines.append("- PASS: no README quality anomalies detected")
    lines.append("")
    lines.append("## 5. Status Language Findings")
    lines.append("")
    if status_findings:
        for item in status_findings:
            lines.append(f"- CHECK: {item}")
    else:
        lines.append("- PASS: no status language anomalies detected")
    lines.append("")
    lines.append("## 6. Domain Fragmentation Candidates")
    lines.append("")
    if domain_findings:
        for item in domain_findings:
            lines.append(f"- REVIEW: {item}")
    else:
        lines.append("- PASS: no domain fragmentation candidates detected")
    lines.append("")
    lines.append("## 7. Duplicate Hash Groups")
    lines.append("")
    if duplicate_hashes:
        for digest, paths in sorted(duplicate_hashes.items(), key=lambda item: (-len(item[1]), item[0]))[:50]:
            lines.append(f"### {digest}")
            lines.append("")
            for path in paths:
                lines.append(f"- {path.relative_to(ROOT).as_posix()} ({file_size(path)} bytes)")
            lines.append("")
    else:
        lines.append("- PASS: no duplicate file hashes detected")
    lines.append("")
    lines.append("## 8. Large Files")
    lines.append("")
    if large_files:
        for path in sorted(large_files, key=file_size, reverse=True)[:100]:
            lines.append(f"- {path.relative_to(ROOT).as_posix()} ({file_size(path)} bytes)")
    else:
        lines.append("- PASS: no large files over threshold detected")
    lines.append("")
    lines.append("## 9. Generated Duplicate Candidates")
    lines.append("")
    if generated_duplicate_candidates:
        for path in generated_duplicate_candidates[:100]:
            lines.append(f"- {path.relative_to(ROOT).as_posix()}")
    else:
        lines.append("- PASS: no generated duplicate candidates detected")
    lines.append("")
    lines.append("## 10. Cleanup Policy")
    lines.append("")
    lines.append("Do not delete scenario evidence artifacts automatically.")
    lines.append("Do not delete lab evidence boundary notes automatically.")
    lines.append("Only remove duplicates after confirming they are not reviewer-facing evidence, generated indexes, or validation summaries.")
    lines.append("")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(f"[OK] wrote {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())