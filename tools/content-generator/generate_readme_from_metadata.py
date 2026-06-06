from pathlib import Path
import yaml


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def render_list(items) -> str:
    if not items:
        return "- None currently defined."
    return "\n".join(f"- {item}" for item in items)


def render_table_rows(items) -> str:
    if not items:
        return "| None | None currently defined |\n"

    rows = []
    for item in items:
        if isinstance(item, dict):
            name = item.get("name", "Unnamed Component")
            purpose = item.get("purpose", "Provides operational context")
            rows.append(f"| {name} | {purpose} |")
        else:
            rows.append(f"| {item} | Provides operational context |")
    return "\n".join(rows)


def render_related(items) -> str:
    if not items:
        return "None currently defined."
    return "\n".join(f"- {item}" for item in items)


def render_readme(data: dict) -> str:
    related = data.get("related_scenarios", {}) or {}

    return f"""# {data.get("scenario_title", data.get("scenario_name", "Scenario"))}

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | {data.get("scenario_name", "")} |
| Lifecycle Level | {data.get("lifecycle_level", "")} |
| Scenario Path | {data.get("scenario_path", "")} |
| Scenario Type | {data.get("scenario_type", "")} |
| Primary Domain | {data.get("primary_domain", "")} |
| Status | {data.get("status", "draft")} |

---

## Overview

{data.get("overview", "").strip()}

---

## Objectives

{render_list(data.get("objectives", []))}

---

## Scenario Architecture

![Operational Poster](diagrams/operational-poster.png)

---

## Used Modules

{render_list(data.get("used_modules", []))}

---

## Used Adapters

{render_list(data.get("used_adapters", []))}

---

## Infrastructure Components

{render_list(data.get("infrastructure_components", []))}

---

## Operational Workflow

The scenario follows the infrastructure operations lifecycle:

1. Detection
2. Correlation and Analysis
3. Incident Coordination
4. Recovery and Automation
5. Recovery Validation
6. Governance and Reporting

---

## Detection Workflow

{data.get("detection_workflow", "").strip()}

---

## Correlation and Analysis

{data.get("correlation_and_analysis", "").strip()}

---

## Alert and Incident Workflow

{data.get("alert_and_incident_workflow", "").strip()}

---

## Recovery and Automation Workflow

{data.get("recovery_and_automation_workflow", "").strip()}

---

## Recovery Validation

{data.get("recovery_validation", "").strip()}

---

## Monitoring and Visibility

{data.get("monitoring_and_visibility", "").strip()}

---

## Operational Components

| Component | Purpose |
|---|---|
{render_table_rows(data.get("operational_components", []))}

---

## Evidence

- [Evidence Summary](evidence/generated/summary.md)
- [Execution Evidence](evidence/generated/execution-evidence.md)
- [Validation Evidence](evidence/generated/validation-evidence.md)
- [Artifact Manifest](evidence/generated/artifact-manifest.json)
- [Artifact Checksums](evidence/generated/artifact-checksums.json)

---

## Expected Outcomes

{render_list(data.get("expected_outcomes", []))}

---

## Validation Checklist

{render_list([f"[ ] {item}" for item in data.get("validation_checklist", [])])}

---

## Related Scenarios

### Upstream Scenarios

{render_related(related.get("upstream", []))}

### Same-Level Scenarios

{render_related(related.get("same_level", []))}

### Downstream Scenarios

{render_related(related.get("downstream", []))}

### Cross-Domain Scenarios

{render_related(related.get("cross_domain", []))}

---

## Summary

This scenario contributes to the infrastructure operations portfolio by documenting {data.get("primary_domain", "infrastructure").lower()} workflow design, telemetry interpretation, lifecycle execution, validation criteria, and reviewable operational evidence.
"""


def main() -> None:
    count = 0

    for metadata_path in sorted(Path("scenarios").glob("level-*/*/metadata.yaml")):
        data = load_yaml(metadata_path)
        readme_path = metadata_path.parent / "README.md"
        readme_path.write_text(render_readme(data).rstrip() + "\n", encoding="utf-8")
        print(f"[OK] {readme_path}")
        count += 1

    print(f"[DONE] generated README files: {count}")


if __name__ == "__main__":
    main()
