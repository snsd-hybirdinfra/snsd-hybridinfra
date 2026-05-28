from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parents[3]
        / "tools"
    )
)

from shared_runtime.src.runtime_encoding import (
    configure_runtime_encoding
)

configure_runtime_encoding()

from src.topology_inference import (
    infer_topology
)


REPO_ROOT = Path(__file__).resolve().parents[3]

SCENARIOS_ROOT = (
    REPO_ROOT
    / "scenarios"
)


def discover_scenario_dirs():

    scenario_dirs = []

    for level_dir in sorted(
        SCENARIOS_ROOT.glob(
            "level-*"
        )
    ):

        if not level_dir.is_dir():

            continue

        for scenario_dir in sorted(
            level_dir.iterdir()
        ):

            if scenario_dir.is_dir():

                scenario_dirs.append(
                    scenario_dir
                )

    return scenario_dirs


def infer_metadata(
    scenario_dir: Path
):

    lifecycle_level = scenario_dir.parent.name
    scenario_name = scenario_dir.name

    return {
        "scenario_name": scenario_name,
        "lifecycle_level": lifecycle_level,
        "scenario_title": scenario_name.replace(
            "-",
            " "
        ).title()
    }


def render_yaml_list(
    key: str,
    items: list
):

    lines = [
        f"{key}:"
    ]

    for item in items:

        if "id" in item:

            lines.append(
                f"  - id: {item['id']}"
            )

            for field, value in item.items():

                if field == "id":

                    continue

                lines.append(
                    f"    {field}: {value}"
                )

            continue

        first = True

        for field, value in item.items():

            if first:

                lines.append(
                    f"  - {field}: {value}"
                )

                first = False

                continue

            lines.append(
                f"    {field}: {value}"
            )

    return lines


def ensure_metadata(
    scenario_dir: Path,
    metadata: dict
):

    metadata_path = (
        scenario_dir
        / "metadata.yaml"
    )

    if metadata_path.exists():

        return "SKIPPED"

    content = [
        f"scenario_name: {metadata['scenario_name']}",
        f"lifecycle_level: {metadata['lifecycle_level']}",
        "status: draft",
        "source: inferred-from-repository-structure",
        ""
    ]

    metadata_path.write_text(
        "\n".join(
            content
        ),
        encoding="utf-8"
    )

    return "GENERATED"


def ensure_diagram_specs(
    scenario_dir: Path,
    metadata: dict
):

    diagrams_dir = (
        scenario_dir
        / "diagrams"
    )

    diagrams_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    generated = 0
    skipped = 0

    for diagram_name in [
        "architecture-overview",
        "workflow-overview",
        "relationship-overview"
    ]:

        spec_path = (
            diagrams_dir
            / f"{diagram_name}.spec.yaml"
        )

        if spec_path.exists():

            skipped += 1
            continue

        content = [
            "diagram:",
            f"  type: {diagram_name}",
            f"  title: {metadata['scenario_title']} - {diagram_name}",
            "",
            f"  scenario: {metadata['scenario_name']}",
f"  lifecycle: {metadata['lifecycle_level']}",
            "  layout: left-to-right",
            "",
            *render_yaml_list(
                "nodes",
                infer_topology(
                    metadata["scenario_name"],
                    metadata["lifecycle_level"]
                )[0]
            ),
            *render_yaml_list(
                "edges",
                infer_topology(
                    metadata["scenario_name"],
                    metadata["lifecycle_level"]
                )[1]
            ),
            ""
        ]

        spec_path.write_text(
            "\n".join(
                content
            ),
            encoding="utf-8"
        )

        generated += 1

    return generated, skipped


def ensure_readme(
    scenario_dir: Path,
    metadata: dict
):

    readme_path = (
        scenario_dir
        / "README.md"
    )

    if readme_path.exists():

        return "SKIPPED"

    content = f"""# {metadata['scenario_title']}

## Scenario Metadata

| Field | Value |
|---|---|
| Scenario Name | {metadata['scenario_name']} |
| Lifecycle Level | {metadata['lifecycle_level']} |
| Source | Inferred from repository structure |

## Scenario Architecture

![Architecture Overview](./diagrams/architecture-overview.png)

## Used Modules

TBD

## Infrastructure Components

TBD

## Operational Workflow

TBD

## Related Scenarios

### Previous Scenarios

TBD

### Next Scenarios

TBD

## Governance Notes

This scenario package was initialized by the repo-aware scenario normalizer.
"""

    readme_path.write_text(
        content,
        encoding="utf-8"
    )

    return "GENERATED"


def normalize_scenario(
    scenario_dir: Path
):

    metadata = infer_metadata(
        scenario_dir
    )

    metadata_status = ensure_metadata(
        scenario_dir,
        metadata
    )

    readme_status = ensure_readme(
        scenario_dir,
        metadata
    )

    diagram_generated, diagram_skipped = ensure_diagram_specs(
        scenario_dir,
        metadata
    )

    return {
        "scenario": metadata["scenario_name"],
        "level": metadata["lifecycle_level"],
        "metadata": metadata_status,
        "readme": readme_status,
        "diagram_specs_generated": diagram_generated,
        "diagram_specs_skipped": diagram_skipped
    }


def main():

    scenario_dirs = discover_scenario_dirs()

    print(
        f"Discovered scenario folders: {len(scenario_dirs)}"
    )

    results = []

    for scenario_dir in scenario_dirs:

        result = normalize_scenario(
            scenario_dir
        )

        results.append(
            result
        )

        print(
            f"[NORMALIZE] {result['level']} / {result['scenario']} "
            f"metadata={result['metadata']} "
            f"readme={result['readme']} "
            f"diagram_specs_generated={result['diagram_specs_generated']} "
            f"diagram_specs_skipped={result['diagram_specs_skipped']}"
        )

    print(
        f"Scenario normalization completed. "
        f"Scenario folders checked: {len(results)}"
    )


if __name__ == "__main__":
    main()








