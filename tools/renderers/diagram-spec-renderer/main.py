import sys
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parents[3]

if len(sys.argv) < 2:
    raise ValueError(
        "Usage: python main.py <spec-path>"
    )

SPEC_PATH = Path(sys.argv[1]).resolve()

OUTPUT_PATH = SPEC_PATH.with_suffix("").with_suffix(".svg")


STYLE = {
    "telemetry-source": "#2563eb",
    "telemetry-pipeline": "#0891b2",
    "analysis-layer": "#7c3aed",
    "alert-layer": "#ea580c",
    "evidence-layer": "#16a34a"
}

def export_png(svg_path: Path):

    png_path = svg_path.with_suffix(".png")

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch()

        page = browser.new_page(
            viewport={
                "width": 1600,
                "height": 900
            }
        )

        page.goto(svg_path.resolve().as_uri())

        page.screenshot(
            path=str(png_path)
        )

        browser.close()

    print(f"Generated PNG: {png_path}")


def load_yaml(path: Path):

    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def render_svg(spec: dict):

    nodes = spec["nodes"]
    edges = spec["edges"]

    positions = {}

    for index, node in enumerate(nodes):
        positions[node["id"]] = {
            "x": 80 + index * 260,
            "y": 220
        }

    width = max(1200, 220 + len(nodes) * 260)
    height = 520

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#0f172a" />',
        f'<text x="40" y="55" fill="#ffffff" font-size="28" font-weight="bold">{spec["diagram"]["scenario"]}</text>',
        f'<text x="40" y="90" fill="#cbd5e1" font-size="15">{spec["diagram"]["lifecycle"]}</text>'
    ]

    for edge in edges:
        source = positions[edge["from"]]
        target = positions[edge["to"]]

        lines.append(
            f'<line x1="{source["x"] + 200}" y1="{source["y"] + 35}" '
            f'x2="{target["x"]}" y2="{target["y"] + 35}" '
            f'stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />'
        )

        mid_x = (source["x"] + target["x"]) / 2 + 70

        lines.append(
            f'<text x="{mid_x}" y="{source["y"] + 20}" fill="#cbd5e1" font-size="12">'
            f'{edge.get("label", edge["type"])}</text>'
        )

    lines.insert(
        3,
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" '
        'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" /></marker></defs>'
    )

    for node in nodes:
        pos = positions[node["id"]]
        fill = STYLE.get(node["type"], "#334155")

        lines.append(
            f'<rect x="{pos["x"]}" y="{pos["y"]}" width="200" height="70" rx="12" '
            f'fill="{fill}" stroke="#e2e8f0" stroke-width="1.5" />'
        )

        lines.append(
            f'<text x="{pos["x"] + 16}" y="{pos["y"] + 32}" fill="#ffffff" '
            f'font-size="14" font-weight="bold">{node["label"]}</text>'
        )

        lines.append(
            f'<text x="{pos["x"] + 16}" y="{pos["y"] + 54}" fill="#e2e8f0" '
            f'font-size="11">{node["type"]}</text>'
        )

    lines.append("</svg>")

    return "\n".join(lines)


def main():

    spec = load_yaml(SPEC_PATH)
    svg = render_svg(spec)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(svg)

    print(f"Generated SVG: {OUTPUT_PATH}")

    export_png(OUTPUT_PATH)


if __name__ == "__main__":
    main()
