from models.diagram_model import DiagramModel


def parse_diagram(data: dict) -> DiagramModel:

    return DiagramModel(
        scenario_name=data.get(
            "scenario_name",
            data.get("topology_name", "")
        ),

        lifecycle_level=data["lifecycle_level"],

        title=data.get(
            "title",
            data.get("topology_name", "")
        ),

        diagram_type=data.get(
            "diagram_type",
            "topology-architecture"
        ),

        output_name=data.get(
            "output_name",
            "topology-architecture"
        ),

        modules=data.get("modules", []),
        adapters=data.get("adapters", []),
        workflow_steps=data.get("workflow_steps", []),

        topology_nodes=data.get("nodes", []),
        topology_edges=data.get("edges", [])
    )
