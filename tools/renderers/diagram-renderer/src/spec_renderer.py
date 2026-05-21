import sys
import yaml

from pathlib import Path
from playwright.sync_api import sync_playwright


REPO_ROOT = Path(__file__).resolve().parents[3]


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
    "evidence-layer": "#16a34a"
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
    }
}


LAYER_Y = {
    "infrastructure": 140,
    "telemetry": 260,
    "analysis": 380,
    "operational": 500,
    "evidence": 620
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


def render_svg(spec: dict):

    nodes = spec["nodes"]
    edges = spec["edges"]

    positions = {}

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

    width = 2200
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

        lines.append(
            f'<line '
            f'x1="{source["x"] + 240}" '
            f'y1="{source["y"] + 40}" '
            f'x2="{target["x"]}" '
            f'y2="{target["y"] + 40}" '
            f'stroke="{edge_style["color"]}" '
            f'stroke-width="{edge_style["width"]}" '
            f'stroke-dasharray="{edge_style["dasharray"]}" '
            f'marker-end="url(#arrow)" />'
        )

        mid_x = (
            source["x"] + target["x"]
        ) / 2 + 120

        mid_y = (
            source["y"] + target["y"]
        ) / 2 - 18

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