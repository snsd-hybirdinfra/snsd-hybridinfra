from pathlib import Path
import sys

from src.loader import load_yaml
from src.validator import validate_metadata
from src.parser import parse_scenario_metadata
from src.exporter import export_metadata

from src.template_renderer import render_template
from src.template_resolver import resolve_level_template

from src.diagram_spec_generator import (
    generate_level_1_specs
)

from src.diagram_renderer_bridge import (
    render_scenario_diagrams
)


REPO_ROOT = Path(__file__).resolve().parents[3]

SCHEMA_PATH = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
    / "schemas"
    / "scenario-schema.yaml"
)

DEFAULT_EXAMPLE_PATH = (
    "examples/vpn-connectivity-monitoring.yaml"
)

SCENARIO_ROOT = (
    REPO_ROOT
    / "scenarios"
)


def resolve_input_path():

    if len(sys.argv) > 1:

        return sys.argv[1]

    return DEFAULT_EXAMPLE_PATH


def create_scenario_structure(
    base_path: Path
):

    directories = [

        "architecture",
        "implementation",
        "evidence",
        "artifacts",
        "diagrams"
    ]

    for directory in directories:

        (base_path / directory).mkdir(
            parents=True,
            exist_ok=True
        )


def generate_diagram_specs(
    scenario_path: Path,
    exported: dict
):

    lifecycle_level = exported[
        "lifecycle_level"
    ]

    scenario_name = exported[
        "scenario_name"
    ]

    if lifecycle_level == "level-1-visibility":

        generate_level_1_specs(
            scenario_path,
            scenario_name
        )

        return

    print(
        f"Diagram spec generation skipped "
        f"for lifecycle: {lifecycle_level}"
    )


def main():

    input_path = resolve_input_path()

    print(
        f"Scenario input: "
        f"{input_path}"
    )

    raw_data = load_yaml(
        input_path
    )

    validate_metadata(
        raw_data,
        str(SCHEMA_PATH)
    )

    metadata = parse_scenario_metadata(
        raw_data
    )

    exported = export_metadata(
        metadata
    )

    resolve_level_template(
        exported["lifecycle_level"]
    )

    rendered = render_template(
        "templates",
        f"levels/{exported['lifecycle_level']}/readme.md.j2",
        exported
    )

    scenario_path = (

    SCENARIO_ROOT

    / exported["lifecycle_level"]

    / exported["scenario_name"]
    )

    scenario_path.mkdir(
        parents=True,
        exist_ok=True
    )

    create_scenario_structure(
        scenario_path
    )

    readme_path = (
        scenario_path
        / "README.md"
    )

    with open(
        readme_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(rendered)

    print(
        f"Scenario README generated: "
        f"{readme_path}"
    )

    generate_diagram_specs(
        scenario_path,
        exported
    )

    render_scenario_diagrams(
        scenario_path
    )

    print(
        f"Scenario package generated: "
        f"{scenario_path}"
    )

    print(
        "Scenario generation completed."
    )


if __name__ == "__main__":
    main()
