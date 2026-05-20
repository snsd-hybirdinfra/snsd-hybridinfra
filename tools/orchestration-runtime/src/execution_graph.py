from pathlib import Path
import json


def load_json(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def build_execution_graph(
    run_context: dict
):

    run_path = Path(
        run_context["workspace"]
    )

    artifacts_path = (
        run_path
        / "artifacts.json"
    )

    lineage_path = (
        run_path
        / "artifact-lineage.json"
    )

    artifacts = []

    lineage = []

    if artifacts_path.exists():

        artifacts = load_json(
            artifacts_path
        )

    if lineage_path.exists():

        lineage = load_json(
            lineage_path
        )

    nodes = []
    edges = []

    tool_names = set()

    for artifact in artifacts:

        tool_names.add(
            artifact["produced_by"]
        )

        nodes.append({
            "id": artifact["artifact_id"],
            "type": "artifact",
            "label": artifact["artifact_type"],
            "path": artifact["artifact_path"]
        })

    for tool_name in sorted(tool_names):

        nodes.append({
            "id": tool_name,
            "type": "tool",
            "label": tool_name
        })

    for artifact in artifacts:

        edges.append({
            "source": artifact["produced_by"],
            "target": artifact["artifact_id"],
            "relationship": "produced"
        })

    for handoff in lineage:

        nodes.append({
            "id": handoff["target_tool"],
            "type": "tool",
            "label": handoff["target_tool"]
        })

        edges.append({
            "source": handoff["artifact_id"],
            "target": handoff["target_tool"],
            "relationship": handoff["handoff_type"]
        })

    graph = {
        "run_id": run_context["run_id"],
        "nodes": nodes,
        "edges": edges
    }

    graph_path = (
        run_path
        / "execution-graph.json"
    )

    with open(
        graph_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            graph,
            file,
            indent=2
        )

    return graph_path
