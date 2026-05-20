from pathlib import Path
import json


def load_json(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def render_execution_graph(
    run_context: dict
):

    run_path = Path(
        run_context["workspace"]
    )

    graph_path = (
        run_path
        / "execution-graph.json"
    )

    output_path = (
        run_path
        / "execution-graph.svg"
    )

    graph = load_json(
        graph_path
    )

    nodes = graph["nodes"]
    edges = graph["edges"]

    node_positions = {}

    tool_nodes = [
        node for node in nodes
        if node["type"] == "tool"
    ]

    artifact_nodes = [
        node for node in nodes
        if node["type"] == "artifact"
    ]

    for index, node in enumerate(tool_nodes):

        node_positions[node["id"]] = {
            "x": 100,
            "y": 120 + index * 90
        }

    for index, node in enumerate(artifact_nodes):

        node_positions[node["id"]] = {
            "x": 500,
            "y": 120 + index * 90
        }

    height = max(
        500,
        180 + max(len(tool_nodes), len(artifact_nodes)) * 90
    )

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}">',
        '<rect width="100%" height="100%" fill="#0f172a" />',
        '<text x="40" y="50" fill="#ffffff" font-size="26" font-weight="bold">Execution Graph</text>'
    ]

    for edge in edges:

        source = node_positions.get(
            edge["source"]
        )

        target = node_positions.get(
            edge["target"]
        )

        if not source or not target:

            continue

        lines.append(
            f'<line x1="{source["x"] + 220}" y1="{source["y"] + 20}" '
            f'x2="{target["x"]}" y2="{target["y"] + 20}" '
            f'stroke="#94a3b8" stroke-width="2" />'
        )

        lines.append(
            f'<text x="{source["x"] + 250}" y="{source["y"] + 10}" '
            f'fill="#cbd5e1" font-size="12">{edge["relationship"]}</text>'
        )

    for node in tool_nodes:

        pos = node_positions[node["id"]]

        lines.append(
            f'<rect x="{pos["x"]}" y="{pos["y"]}" width="220" height="48" '
            f'rx="10" fill="#1f2937" stroke="#60a5fa" stroke-width="2" />'
        )

        lines.append(
            f'<text x="{pos["x"] + 16}" y="{pos["y"] + 30}" '
            f'fill="#ffffff" font-size="14">{node["label"]}</text>'
        )

    for node in artifact_nodes:

        pos = node_positions[node["id"]]

        lines.append(
            f'<rect x="{pos["x"]}" y="{pos["y"]}" width="260" height="48" '
            f'rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2" />'
        )

        lines.append(
            f'<text x="{pos["x"] + 16}" y="{pos["y"] + 30}" '
            f'fill="#ffffff" font-size="14">{node["label"]}</text>'
        )

    lines.append("</svg>")

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "\n".join(lines)
        )

    return output_path
