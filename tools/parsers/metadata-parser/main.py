from pathlib import Path

from src.loader import load_yaml
from src.validator import validate_metadata
from src.parser import parse_scenario_metadata
from src.exporter import export_metadata
from src.template_renderer import render_template


SCHEMA_PATH = "schemas/scenario-schema.yaml"
EXAMPLE_PATH = "examples/vpn-connectivity-monitoring.yaml"

TEMPLATE_DIR = "../../generators/scenario-generator/templates/scenario"

SCENARIO_ROOT = "../../../scenarios"


def main():

    raw_data = load_yaml(EXAMPLE_PATH)

    validate_metadata(
        raw_data,
        SCHEMA_PATH
    )

    metadata = parse_scenario_metadata(raw_data)

    exported = export_metadata(metadata)

    rendered = render_template(
        TEMPLATE_DIR,
        exported["readme_template"],
        exported
    )

    scenario_path = Path(
        SCENARIO_ROOT
    ) / exported["lifecycle_level"] / exported["scenario_name"]

    readme_path = scenario_path / "README.md"

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(rendered)

    print(f"README generated: {readme_path}")


if __name__ == "__main__":
    main()
