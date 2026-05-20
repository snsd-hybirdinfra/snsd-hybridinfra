from pathlib import Path

from src.loader import load_yaml
from src.renderer import parse_diagram
from src.template_renderer import render_template

from src.exporter import export_svg
from src.exporter import export_png

from src.layout_engine import build_layout


REPO_ROOT = Path(__file__).resolve().parents[3]


TOPOLOGY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "schemas"
    / "topology"
    / "examples"
    / "vpn-connectivity-topology.yaml"
)

TEMPLATE_DIR = "templates/topology"

TEMPLATE_NAME = "topology-architecture.svg.j2"

OUTPUT_DIR = (
    REPO_ROOT
    / "tools"
    / "renderers"
    / "diagram-renderer"
    / "outputs"
)


def main():

    raw_data = load_yaml(
        str(TOPOLOGY_PATH)
    )

    model = parse_diagram(
        raw_data
    )

    layout = build_layout(
        model.topology_nodes
    )

    context = {

        "title":
            model.title,

        "topology_nodes":
            model.topology_nodes,

        "topology_edges":
            model.topology_edges,

        "layers":
            layout["layers"],

        "layer_positions":
            layout["layer_positions"],

        "node_positions":
            layout["node_positions"],

        "canvas_width":
            layout["canvas_width"],

        "canvas_height":
            layout["canvas_height"]
    }

    rendered = render_template(
        TEMPLATE_DIR,
        TEMPLATE_NAME,
        context
    )

    svg_path = (
        OUTPUT_DIR
        / "topology-architecture.svg"
    )

    png_path = (
        OUTPUT_DIR
        / "topology-architecture.png"
    )

    export_svg(
        svg_path,
        rendered
    )

    export_png(
        svg_path,
        png_path
    )

    print(
        "Topology diagram rendered."
    )

    print(
        f"Canvas width: "
        f"{layout['canvas_width']}"
    )

    print(
        f"Canvas height: "
        f"{layout['canvas_height']}"
    )

    print(
        f"SVG Output: {svg_path}"
    )

    print(
        f"PNG Output: {png_path}"
    )


if __name__ == "__main__":
    main()
