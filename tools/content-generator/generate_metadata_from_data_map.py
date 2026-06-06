from pathlib import Path
import csv
import textwrap


INPUT = Path("reports/scenario-required-data-map.csv")


def split_semicolon(value: str) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(";") if item.strip()]


def yaml_list(items: list[str], indent: int = 2) -> str:
    prefix = " " * indent
    if not items:
        return f"{prefix}[]"
    return "\n".join(f"{prefix}- {item}" for item in items)


def block(value: str, indent: int = 2) -> str:
    prefix = " " * indent
    wrapped = textwrap.fill(
        value.strip(),
        width=100,
        subsequent_indent="",
        replace_whitespace=True,
    )
    return "\n".join(prefix + line for line in wrapped.splitlines())


def build_overview(row: dict) -> str:
    title = row["scenario_title"]
    domain = row["primary_domain"]
    target = row["target_resource"]
    focus = row["operational_focus"]

    return (
        f"This scenario documents {title.lower()} within the {domain.lower()} operational domain. "
        f"It focuses on {target} and demonstrates how infrastructure operations teams can use "
        f"domain-specific telemetry, lifecycle workflow design, and evidence-backed validation to support "
        f"{focus.lower()}."
    )


def build_objectives(row: dict) -> list[str]:
    domain = row["primary_domain"]
    target = row["target_resource"]
    signals = split_semicolon(row["telemetry_signals"])

    objectives = [
        f"Define the scenario-specific {row['primary_domain'].lower()} signal represented by {row['scenario_name']}.",
        f"Identify the affected {domain.lower()} components and dependencies.",
        f"Collect and interpret telemetry from {target}.",
    ]

    for signal in signals[:3]:
        objectives.append(f"Use {signal} as an operational signal for detection or validation.")

    objectives.extend([
        "Document the lifecycle workflow from detection through validation.",
        "Produce reviewer-readable evidence artifacts for portfolio assessment.",
    ])

    return objectives


def build_operational_components(row: dict) -> list[tuple[str, str]]:
    components = split_semicolon(row["infrastructure_components"])
    result = []

    for component in components:
        result.append((component, f"Provides context or signal source for {row['primary_domain']} operations"))

    result.extend([
        ("Detection Logic", "Identifies abnormal or degraded operational conditions"),
        ("Correlation Logic", "Connects related signals, dependencies, and impact context"),
        ("Validation Method", "Confirms stable state, restored condition, or visibility completeness"),
        ("Evidence Output", "Records public-safe completion and review artifacts"),
    ])

    seen = set()
    deduped = []
    for name, purpose in result:
        key = name.lower()
        if key not in seen:
            seen.add(key)
            deduped.append((name, purpose))

    return deduped


def render_metadata(row: dict) -> str:
    objectives = build_objectives(row)
    signals = split_semicolon(row["telemetry_signals"])
    components = split_semicolon(row["infrastructure_components"])
    modules = split_semicolon(row["used_modules"])
    adapters = split_semicolon(row["used_adapters"])
    evidence = split_semicolon(row["evidence_outputs"])
    op_components = build_operational_components(row)

    op_component_yaml = "\n".join(
        f"  - name: {name}\n    purpose: {purpose}"
        for name, purpose in op_components
    )

    content = f"""scenario_name: {row['scenario_name']}
scenario_title: {row['scenario_title']}
lifecycle_level: {row['lifecycle_level']}
scenario_path: {row['scenario_path']}
scenario_type: {row['scenario_type']}
primary_domain: {row['primary_domain']}
status: draft

overview: |
{block(build_overview(row), 2)}

objectives:
{yaml_list(objectives, 2)}

operational_focus: |
{block(row['operational_focus'], 2)}

target_resource: |
{block(row['target_resource'], 2)}

telemetry_signals:
{yaml_list(signals, 2)}

infrastructure_components:
{yaml_list(components, 2)}

detection_workflow: |
{block(row['detection_inputs'], 2)}

correlation_and_analysis: |
{block(row['correlation_context'], 2)}

alert_and_incident_workflow: |
{block(row['incident_or_response_flow'], 2)}

recovery_and_automation_workflow: |
{block(row['incident_or_response_flow'], 2)}

recovery_validation: |
{block(row['recovery_or_validation_actions'], 2)}

monitoring_and_visibility: |
{block("Monitoring and visibility include " + row['telemetry_signals'] + ".", 2)}

used_modules:
{yaml_list(modules, 2)}

used_adapters:
{yaml_list(adapters, 2)}

operational_components:
{op_component_yaml}

evidence_outputs:
{yaml_list(evidence, 2)}

expected_outcomes:
  - The scenario has domain-specific operational context.
  - Telemetry signals are identified and mapped to the scenario purpose.
  - Infrastructure components and dependencies are documented.
  - Lifecycle workflow sections are populated with scenario-specific content.
  - Validation and evidence outputs are defined for portfolio review.

validation_checklist:
  - Scenario metadata is present.
  - Operational poster reference is preserved.
  - Used modules are listed.
  - Used adapters are listed.
  - Detection workflow is scenario-specific.
  - Correlation and analysis workflow is scenario-specific.
  - Response or recovery workflow is described.
  - Recovery validation is described.
  - Evidence links are present.
  - Deprecated diagram references are not used.

related_scenarios:
  upstream: []
  same_level: []
  downstream: []
  cross_domain: []
"""

    return content.rstrip() + "\n"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"missing input file: {INPUT}")

    with INPUT.open("r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    count = 0

    for row in rows:
        scenario_path = Path(row["scenario_path"])
        if not scenario_path.exists():
            print(f"[SKIP] missing scenario path: {scenario_path}")
            continue

        metadata_path = scenario_path / "metadata.yaml"
        metadata_path.write_text(render_metadata(row), encoding="utf-8")
        print(f"[OK] {metadata_path}")
        count += 1

    print(f"[DONE] generated metadata files: {count}")


if __name__ == "__main__":
    main()

