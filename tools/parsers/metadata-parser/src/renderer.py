from models.diagram_model import DiagramModel


def parse_diagram(data: dict) -> DiagramModel:

    return DiagramModel(
        scenario_name=data["scenario_name"],
        lifecycle_level=data["lifecycle_level"],
        title=data["title"],
        diagram_type=data["diagram_type"],

        modules=data.get("modules", []),
        adapters=data.get("adapters", []),
        workflow_steps=data.get("workflow_steps", []),

        output_name=data.get(
            "output_name",
            "diagram"
        )
    )
