from pathlib import Path
import json


def load_json(path: Path):

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def render_execution_graph(run_context: dict):

    run_path = Path(run_context["workspace"])
    graph_path = run_path / "execution-graph.json"
    svg_path = run_path / "execution-graph.svg"

    graph = load_json(graph_path)

    with open(svg_path, "w", encoding="utf-8") as file:
        file.write(
            '<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="500">'
            '<rect width="100%" height="100%" fill="#0f172a" />'
            '<text x="40" y="50" fill="#ffffff" font-size="26" font-weight="bold">'
            'Execution Graph'
            '</text>'
            '</svg>'
        )

    return {
        "svg": svg_path
    }
