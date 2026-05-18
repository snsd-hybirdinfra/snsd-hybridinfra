from pathlib import Path

from src.loader import load_yaml
from src.validator import validate_relationship_graph
from src.parser import parse_relationship_graph
from src.exporter import export_relationship_graph
from src.template_renderer import render_template


SCHEMA_PATH = "schemas/scenario-relationship-schema.yaml"

EXAMPLE_PATH = (
    "examples/vpn-relationship-graph.yaml"
)

TEMPLATE_DIR = "templates"

TEMPLATE_NAME = "relationship-graph.md.j2"

OUTPUT_DIR = "outputs/graphs"


def main():

    raw_data = load_yaml(EXAMPLE_PATH)

    validate_relationship_graph(
        raw_data,
        SCHEMA_PATH
    )

    graph = parse_relationship_graph(raw_data)

    exported = export_relationship_graph(graph)

    rendered = render_template(
        TEMPLATE_DIR,
        TEMPLATE_NAME,
        exported
    )

    output_path = Path(
        OUTPUT_DIR
    ) / f"{exported['scenario_name']}.md"

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(rendered)

    print(
        f"Relationship graph generated: {output_path}"
    )


if __name__ == "__main__":
    main()
