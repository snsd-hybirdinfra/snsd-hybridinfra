from src.relationship_graph import RelationshipGraph


def parse_relationship_graph(data: dict) -> RelationshipGraph:

    relationships = data.get("relationships", {})

    return RelationshipGraph(

        scenario_name=data["scenario_name"],
        lifecycle_level=data["lifecycle_level"],

        upstream=relationships.get("upstream", []),
        downstream=relationships.get("downstream", []),

        related_visibility=relationships.get(
            "related_visibility",
            []
        ),

        related_correlation=relationships.get(
            "related_correlation",
            []
        ),

        related_recovery=relationships.get(
            "related_recovery",
            []
        ),

        related_resilience=relationships.get(
            "related_resilience",
            []
        ),

        related_continuity=relationships.get(
            "related_continuity",
            []
        ),

        modules=relationships.get("modules", []),
        adapters=relationships.get("adapters", [])
    )
