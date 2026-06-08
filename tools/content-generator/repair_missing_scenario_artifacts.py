from pathlib import Path
import hashlib
import json

ROOT = Path(".").resolve()
SCENARIOS = ROOT / "scenarios"

LEVEL_INFO = {
    "level-1-visibility": {
        "level": "level-1-visibility",
        "lifecycle": "Visibility",
        "modules": ["Telemetry Aggregation Module", "Health Signal Collection Module", "Visibility Reporting Module"],
        "summary": "This scenario documents infrastructure visibility operations using telemetry collection, signal exposure, and operational health reporting.",
    },
    "level-2-correlation": {
        "level": "level-2-correlation",
        "lifecycle": "Correlation and Analysis",
        "modules": ["Telemetry Aggregation Module", "Dependency Correlation Module", "Impact Analysis Module"],
        "summary": "This scenario documents infrastructure correlation operations using telemetry comparison, dependency analysis, and impact reasoning.",
    },
    "level-3-recovery": {
        "level": "level-3-recovery",
        "lifecycle": "Recovery and Automation",
        "modules": ["Recovery Orchestration Module", "Automation Execution Module", "Recovery Validation Module"],
        "summary": "This scenario documents controlled recovery operations using automation execution, restoration workflow control, and recovery validation.",
    },
    "level-4-resilience": {
        "level": "level-4-resilience",
        "lifecycle": "Distributed Resilience",
        "modules": ["Resilience Coordination Module", "Failover Control Module", "Survivability Validation Module"],
        "summary": "This scenario documents distributed resilience operations across failure domains, regions, clusters, or service boundaries.",
    },
    "level-5-continuity": {
        "level": "level-5-continuity",
        "lifecycle": "Enterprise Continuity",
        "modules": ["Continuity Governance Module", "Readiness Assessment Module", "Governance Reporting Module"],
        "summary": "This scenario documents enterprise continuity operations using readiness validation, governance reporting, and cross-domain recovery posture review.",
    },
}

ADAPTERS = ["Prometheus Adapter", "Grafana Adapter", "Ansible Adapter", "Python Exporter Adapter"]

def titleize(name: str) -> str:
    return " ".join(part.capitalize() for part in name.replace("_", "-").split("-"))

def yaml_list(items):
    return "\n".join(f"  - {item}" for item in items)

def write_metadata(scenario_dir: Path, level_name: str):
    info = LEVEL_INFO[level_name]
    name = scenario_dir.name
    title = titleize(name)

    content = f"""scenario_name: {name}
scenario_title: {title}
lifecycle_level: {info["level"]}
lifecycle_name: {info["lifecycle"]}
operational_scope: Infrastructure Operations
environment: Hybrid Infrastructure
status: draft

summary: "{info["summary"]}"

objectives:
  - Document the operational condition represented by {title.lower()}.
  - Identify relevant infrastructure components and telemetry signals.
  - Describe the lifecycle workflow from detection to validation.
  - Produce reviewer-readable evidence and diagram artifacts.

infrastructure_components:
  - Infrastructure target
  - Telemetry source
  - Operational signal
  - Analysis or response workflow
  - Validation output
  - Evidence artifact

used_modules:
{yaml_list(info["modules"])}

used_adapters:
{yaml_list(ADAPTERS)}

related_scenarios: []
"""
    (scenario_dir / "metadata.yaml").write_text(content, encoding="utf-8")

def write_readme(scenario_dir: Path, level_name: str):
    info = LEVEL_INFO[level_name]
    name = scenario_dir.name
    title = titleize(name)

    modules = "\n".join(f"- {module}" for module in info["modules"])
    adapters = "\n".join(f"- {adapter}" for adapter in ADAPTERS)

    content = f"""# {title}

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | `{name}` |
| Lifecycle Level | `{info["level"]}` |
| Lifecycle Name | {info["lifecycle"]} |
| Operational Scope | Infrastructure Operations |
| Environment | Hybrid Infrastructure |
| Status | draft |

---

## Overview

{info["summary"]}

---

## Objectives

- Document the operational condition represented by {title.lower()}.
- Identify relevant infrastructure components and telemetry signals.
- Describe the lifecycle workflow from detection to validation.
- Produce reviewer-readable evidence and diagram artifacts.

---

## Scenario Architecture

This scenario follows the repository operational lifecycle:

Detection -> Correlation & Analysis -> Incident Coordination -> Recovery & Automation -> Recovery Validation -> Governance & Reporting

![Operational Poster](./diagrams/operational-poster.png)

---

## Used Modules

{modules}

---

## Used Adapters

{adapters}

---

## Infrastructure Components

- Infrastructure target
- Telemetry source
- Operational signal
- Analysis or response workflow
- Validation output
- Evidence artifact

---

## Operational Workflow

1. Collect telemetry and infrastructure health signals.
2. Analyze operational symptoms and dependency context.
3. Coordinate incident response or operational review.
4. Execute the appropriate recovery, validation, or governance workflow.
5. Produce evidence for reviewer-readable validation.

---

## Detection

The scenario begins by collecting operational signals from infrastructure targets and telemetry sources.

---

## Correlation & Analysis

Collected signals are correlated with dependency context, infrastructure state, and operational impact.

---

## Alert & Incident Workflow

The workflow defines how the operational condition is reviewed, escalated, and coordinated.

---

## Recovery & Automation

Automation or recovery actions are executed according to the lifecycle level and operational scope.

---

## Recovery Validation

The scenario validates that the expected operational state has been restored or confirmed.

---

## Monitoring & Visibility

Operational visibility is maintained through dashboards, telemetry views, and generated evidence.

---

## Operational Components

| Component | Purpose |
|---|---|
| Infrastructure target | Represents the operational asset or service under review. |
| Telemetry source | Provides health, performance, or event signals. |
| Analysis workflow | Supports correlation and operational reasoning. |
| Response workflow | Supports recovery, coordination, or governance action. |
| Evidence artifact | Records reviewer-readable validation output. |

---

## Evidence

- [Summary](./evidence/generated/summary.md)
- [Execution Evidence](./evidence/generated/execution-evidence.md)
- [Validation Evidence](./evidence/generated/validation-evidence.md)
- [Artifact Manifest](./evidence/generated/artifact-manifest.json)
- [Artifact Checksums](./evidence/generated/artifact-checksums.json)

---

## Validation Checklist

- [ ] Metadata file exists.
- [ ] README file exists.
- [ ] Operational poster exists.
- [ ] Evidence files exist.
- [ ] Scenario is included in repository inventory.
- [ ] Scenario passes repository validation workflow.

---

## Related Scenarios

No directly related scenarios are currently defined for this scenario.

---

## Summary

{title} documents a lifecycle-aligned operational scenario for hybrid infrastructure operations.
"""
    (scenario_dir / "README.md").write_text(content, encoding="utf-8")

def write_svg(scenario_dir: Path, level_name: str):
    info = LEVEL_INFO[level_name]
    title = titleize(scenario_dir.name)
    diagram_dir = scenario_dir / "diagrams"
    diagram_dir.mkdir(parents=True, exist_ok=True)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <rect width="1600" height="900" fill="#020617"/>
  <rect x="70" y="60" width="1460" height="780" rx="28" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="100" y="130" fill="#ffffff" font-size="44" font-family="Arial, sans-serif" font-weight="700">{title}</text>
  <text x="100" y="180" fill="#cbd5e1" font-size="24" font-family="Arial, sans-serif">{info["lifecycle"]} - Hybrid Infrastructure Operations</text>
  <rect x="100" y="240" width="1400" height="110" rx="18" fill="#111827" stroke="#334155"/>
  <text x="130" y="305" fill="#ffffff" font-size="28" font-family="Arial, sans-serif">Detection -> Correlation -> Incident -> Recovery -> Validation -> Governance</text>
  <rect x="100" y="410" width="420" height="300" rx="18" fill="#1e293b"/>
  <rect x="590" y="410" width="420" height="300" rx="18" fill="#1e293b"/>
  <rect x="1080" y="410" width="420" height="300" rx="18" fill="#1e293b"/>
  <text x="130" y="465" fill="#38bdf8" font-size="26" font-family="Arial, sans-serif" font-weight="700">Signals</text>
  <text x="130" y="520" fill="#e5e7eb" font-size="22" font-family="Arial, sans-serif">Telemetry, health state, events</text>
  <text x="620" y="465" fill="#38bdf8" font-size="26" font-family="Arial, sans-serif" font-weight="700">Operational Workflow</text>
  <text x="620" y="520" fill="#e5e7eb" font-size="22" font-family="Arial, sans-serif">Analysis, response, validation</text>
  <text x="1110" y="465" fill="#38bdf8" font-size="26" font-family="Arial, sans-serif" font-weight="700">Evidence</text>
  <text x="1110" y="520" fill="#e5e7eb" font-size="22" font-family="Arial, sans-serif">Reports, checksums, review output</text>
  <text x="100" y="790" fill="#94a3b8" font-size="20" font-family="Arial, sans-serif">SNSD Hybrid Infrastructure - Enterprise Operational Capability Platform</text>
</svg>
"""
    (diagram_dir / "operational-poster.svg").write_text(svg, encoding="utf-8")

def write_evidence(scenario_dir: Path):
    evidence_dir = scenario_dir / "evidence" / "generated"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    title = titleize(scenario_dir.name)

    files = {
        "summary.md": f"# Evidence Summary\n\nThis evidence summary records generated validation context for `{scenario_dir.name}`.\n",
        "execution-evidence.md": f"# Execution Evidence\n\nThis file records the execution evidence location for `{title}`.\n",
        "validation-evidence.md": f"# Validation Evidence\n\nThis file records validation evidence for `{title}`.\n",
    }

    for filename, content in files.items():
        (evidence_dir / filename).write_text(content, encoding="utf-8")

    manifest = {
        "scenario": scenario_dir.name,
        "status": "generated",
        "artifacts": sorted(files.keys()) + ["artifact-manifest.json", "artifact-checksums.json"],
    }

    (evidence_dir / "artifact-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    checksums = {}
    for path in sorted(evidence_dir.iterdir()):
        if path.is_file() and path.name != "artifact-checksums.json":
            checksums[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()

    (evidence_dir / "artifact-checksums.json").write_text(
        json.dumps(checksums, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

repaired = []

for level_dir in sorted(SCENARIOS.iterdir()):
    if not level_dir.is_dir():
        continue

    level_name = level_dir.name
    if level_name not in LEVEL_INFO:
        continue

    for scenario_dir in sorted(level_dir.iterdir()):
        if not scenario_dir.is_dir():
            continue

        changed = False

        if not (scenario_dir / "metadata.yaml").exists():
            write_metadata(scenario_dir, level_name)
            changed = True

        if not (scenario_dir / "README.md").exists():
            write_readme(scenario_dir, level_name)
            changed = True

        if not (scenario_dir / "diagrams" / "operational-poster.svg").exists():
            write_svg(scenario_dir, level_name)
            changed = True

        required_evidence = [
            scenario_dir / "evidence" / "generated" / "summary.md",
            scenario_dir / "evidence" / "generated" / "execution-evidence.md",
            scenario_dir / "evidence" / "generated" / "validation-evidence.md",
            scenario_dir / "evidence" / "generated" / "artifact-manifest.json",
            scenario_dir / "evidence" / "generated" / "artifact-checksums.json",
        ]

        if any(not path.exists() for path in required_evidence):
            write_evidence(scenario_dir)
            changed = True

        if changed:
            repaired.append(scenario_dir.relative_to(ROOT).as_posix())

print(f"[OK] repaired scenarios: {len(repaired)}")
for item in repaired:
    print(f"- {item}")
