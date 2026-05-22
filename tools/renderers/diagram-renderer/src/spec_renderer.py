import sys
import yaml

from pathlib import Path
from playwright.sync_api import sync_playwright


if len(sys.argv) < 2:

    raise ValueError(
        "Usage: python main.py <spec-path>"
    )


SPEC_PATH = Path(
    sys.argv[1]
).resolve()


OUTPUT_PATH = SPEC_PATH.with_suffix(
    ""
).with_suffix(
    ".svg"
)


STYLE = {
    "telemetry-source": "#2563eb",
    "telemetry-pipeline": "#0891b2",
    "analysis-layer": "#7c3aed",
    "alert-layer": "#ea580c",
    "evidence-layer": "#16a34a",

    "scenario-node": "#2563eb",
    "relationship-node": "#64748b",
    "aggregation-node": "#0891b2",
    "convergence-node": "#9333ea",
    "rollup-node": "#16a34a"
}


EDGE_STYLE = {
    "telemetry-flow": {
        "color": "#38bdf8",
        "width": 2,
        "dasharray": ""
    },

    "alert-flow": {
        "color": "#f97316",
        "width": 3,
        "dasharray": ""
    },

    "validation-flow": {
        "color": "#22c55e",
        "width": 2,
        "dasharray": "8,4"
    },

    "evidence-flow": {
        "color": "#cbd5e1",
        "width": 2,
        "dasharray": "4,4"
    },

    "lifecycle-chain": {
        "color": "#94a3b8",
        "width": 2,
        "dasharray": ""
    },

    "aggregation-flow": {
        "color": "#38bdf8",
        "width": 2,
        "dasharray": "6,4"
    },

    "convergence-flow": {
        "color": "#a855f7",
        "width": 3,
        "dasharray": ""
    },

    "rollup-flow": {
        "color": "#22c55e",
        "width": 3,
        "dasharray": "8,4"
    }
}


LAYER_Y = {
    "infrastructure": 140,
    "telemetry": 260,
    "analysis": 380,
    "operational": 500,
    "evidence": 620,
    "detection": 140,
    "correlation": 260,
    "recovery": 260,
    "resilience": 260,
    "failover": 380,
    "continuity": 260,
    "governance": 380,
    "coordination": 500,
    "validation": 500
}


def export_png(svg_path: Path):

    png_path = svg_path.with_suffix(".png")

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch()

        page = browser.new_page(
            viewport={
                "width": 1900,
                "height": 1000
            }
        )

        page.goto(
            svg_path.resolve().as_uri()
        )

        page.screenshot(
            path=str(png_path)
        )

        browser.close()

    print(
        f"Generated PNG: {png_path}"
    )


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def calculate_positions(
    spec: dict,
    nodes: list
):

    diagram_type = spec["diagram"].get(
        "type",
        "architecture-overview"
    )

    positions = {}

    if diagram_type == "relationship-overview":

        base_y = 380

        for node in nodes:

            node_id = node["id"]

            if node_id == "current_scenario":

                positions[node_id] = {
                    "x": 830,
                    "y": base_y
                }

            elif node_id.startswith("previous"):

                positions[node_id] = {
                    "x": 430,
                    "y": base_y
                }

            elif node_id.startswith("next"):

                positions[node_id] = {
                    "x": 1230,
                    "y": base_y
                }

            elif node_id.startswith("aggregation"):

                positions[node_id] = {
                    "x": 430,
                    "y": base_y + 180
                }

            elif node_id.startswith("rollup"):

                positions[node_id] = {
                    "x": 1230,
                    "y": base_y + 180
                }

            elif node_id.startswith("convergence"):

                positions[node_id] = {
                    "x": 830,
                    "y": base_y - 180
                }

            else:

                positions[node_id] = {
                    "x": 830,
                    "y": base_y + 280
                }

        return positions

    layer_counts = {}

    for node in nodes:

        layer = node.get(
            "layer",
            "operational"
        )

        current_index = layer_counts.get(
            layer,
            0
        )

        positions[node["id"]] = {
            "x": 180 + current_index * 420,
            "y": LAYER_Y.get(
                layer,
                500
            )
        }

        layer_counts[layer] = (
            current_index + 1
        )

    return positions


def append_layer_guides(
    lines: list,
    spec: dict,
    diagram_type: str
):

    if diagram_type == "relationship-overview":

        lines.append(
            '<text x="40" y="185" fill="#94a3b8" '
            'font-size="18" font-weight="bold">'
            'Convergence / Governance'
            '</text>'
        )

        lines.append(
            '<text x="40" y="365" fill="#94a3b8" '
            'font-size="18" font-weight="bold">'
            'Lifecycle Chain'
            '</text>'
        )

        lines.append(
            '<text x="40" y="545" fill="#94a3b8" '
            'font-size="18" font-weight="bold">'
            'Aggregation / Rollup'
            '</text>'
        )

        for y in [200, 380, 560]:

            lines.append(
                f'<line x1="40" y1="{y}" '
                f'x2="1800" y2="{y}" '
                f'stroke="#334155" stroke-width="1.5" />'
            )

        return

    for layer in spec.get("layers", []):

        layer_y = LAYER_Y.get(
            layer["id"],
            0
        )

        lines.append(
            f'<text x="40" y="{layer_y - 30}" '
            f'fill="#94a3b8" font-size="18" font-weight="bold">'
            f'{layer["label"]}'
            f'</text>'
        )

        lines.append(
            f'<line x1="40" y1="{layer_y - 12}" '
            f'x2="2100" y2="{layer_y - 12}" '
            f'stroke="#334155" stroke-width="1.5" />'
        )


def get_edge_coordinates(
    diagram_type: str,
    source: dict,
    target: dict
):

    if diagram_type == "relationship-overview":

        return {
            "x1": source["x"] + 120,
            "y1": source["y"] + 40,
            "x2": target["x"] + 120,
            "y2": target["y"] + 40
        }

    return {
        "x1": source["x"] + 240,
        "y1": source["y"] + 40,
        "x2": target["x"],
        "y2": target["y"] + 40
    }


def render_svg(spec: dict):

    nodes = spec["nodes"]
    edges = spec["edges"]

    diagram_type = spec["diagram"].get(
        "type",
        "architecture-overview"
    )

    positions = calculate_positions(
        spec,
        nodes
    )

    width = 1900
    height = 820

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',

        '<rect width="100%" height="100%" fill="#0f172a" />',

        '<defs>'
        '<marker id="arrow" markerWidth="10" markerHeight="10" '
        'refX="9" refY="3" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />'
        '</marker>'
        '</defs>',

        f'<text x="40" y="55" fill="#ffffff" font-size="32" font-weight="bold">'
        f'{spec["diagram"]["scenario"]}'
        f'</text>',

        f'<text x="40" y="92" fill="#cbd5e1" font-size="16">'
        f'{spec["diagram"]["lifecycle"]}'
        f'</text>'
    ]

    append_layer_guides(
        lines,
        spec,
        diagram_type
    )

    for edge in edges:

        source = positions[
            edge["from"]
        ]

        target = positions[
            edge["to"]
        ]

        edge_style = EDGE_STYLE.get(
            edge["type"],
            {
                "color": "#94a3b8",
                "width": 2,
                "dasharray": ""
            }
        )

        coords = get_edge_coordinates(
            diagram_type,
            source,
            target
        )

        lines.append(
            f'<line '
            f'x1="{coords["x1"]}" '
            f'y1="{coords["y1"]}" '
            f'x2="{coords["x2"]}" '
            f'y2="{coords["y2"]}" '
            f'stroke="{edge_style["color"]}" '
            f'stroke-width="{edge_style["width"]}" '
            f'stroke-dasharray="{edge_style["dasharray"]}" '
            f'marker-end="url(#arrow)" />'
        )

        mid_x = (
            coords["x1"] + coords["x2"]
        ) / 2

        mid_y = (
            coords["y1"] + coords["y2"]
        ) / 2 - 14

        lines.append(
            f'<text '
            f'x="{mid_x}" '
            f'y="{mid_y}" '
            f'fill="#cbd5e1" '
            f'font-size="12" '
            f'text-anchor="middle">'
            f'{edge.get("label", edge["type"])}'
            f'</text>'
        )

    for node in nodes:

        pos = positions[
            node["id"]
        ]

        fill = STYLE.get(
            node["type"],
            "#334155"
        )

        lines.append(
            f'<rect '
            f'x="{pos["x"]}" '
            f'y="{pos["y"]}" '
            f'width="240" '
            f'height="80" '
            f'rx="14" '
            f'fill="{fill}" '
            f'stroke="#e2e8f0" '
            f'stroke-width="1.5" />'
        )

        lines.append(
            f'<text '
            f'x="{pos["x"] + 18}" '
            f'y="{pos["y"] + 34}" '
            f'fill="#ffffff" '
            f'font-size="15" '
            f'font-weight="bold">'
            f'{node["label"]}'
            f'</text>'
        )

        lines.append(
            f'<text '
            f'x="{pos["x"] + 18}" '
            f'y="{pos["y"] + 58}" '
            f'fill="#e2e8f0" '
            f'font-size="11">'
            f'{node["type"]}'
            f'</text>'
        )

    lines.append(
        "</svg>"
    )

    return "\n".join(lines)


def main():

    spec = load_yaml(
        SPEC_PATH
    )

    svg = render_svg(
        spec
    )

    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(svg)

    print(
        f"Generated SVG: {OUTPUT_PATH}"
    )

    export_png(
        OUTPUT_PATH
    )


if __name__ == "__main__":
    main()
