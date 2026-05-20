from pathlib import Path
import shutil
import sys

from src.loader import load_yaml
from src.validator import validate_metadata
from src.parser import parse_scenario_metadata
from src.exporter import export_metadata

from src.template_renderer import render_template
from src.template_resolver import resolve_level_template

from src.diagram_runner import (
    run_diagram_renderer
)


SCHEMA_PATH = "schemas/scenario-schema.yaml"

DEFAULT_EXAMPLE_PATH = (
    "examples/vpn-connectivity-monitoring.yaml"
)

SCENARIO_ROOT = "../../../scenarios"

REPO_ROOT = Path(__file__).resolve().parents[3]

RENDERER_OUTPUT = (
    REPO_ROOT
    / "tools"
    / "renderers"
    / "diagram-renderer"
    / "outputs"
    / "topology-architecture.png"
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


def distribute_diagrams(
    scenario_path: Path
):

    diagram_dir = (
        scenario_path
        / "diagrams"
    )

    diagram_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    target_path = (
        diagram_dir
        / "topology-architecture.png"
    )

    if not RENDERER_OUTPUT.exists():

        raise FileNotFoundError(
            f"Rendered PNG not found: "
            f"{RENDERER_OUTPUT}"
        )

    shutil.copy2(
        RENDERER_OUTPUT,
        target_path
    )

    print(
        f"Distributed topology diagram: "
        f"{target_path}"
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
        SCHEMA_PATH
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

        Path(SCENARIO_ROOT)

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
        f"Scenario package generated: "
        f"{scenario_path}"
    )

    print(
        "Invoking diagram renderer..."
    )

    run_diagram_renderer()

    distribute_diagrams(
        scenario_path
    )

    print(
        "Scenario generation completed."
    )


if __name__ == "__main__":
    main()
