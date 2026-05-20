from models.scenario_metadata import ScenarioMetadata


def parse_scenario_metadata(data: dict) -> ScenarioMetadata:

    return ScenarioMetadata(
        scenario_name=data["scenario_name"],
        lifecycle_level=data["lifecycle_level"],
        operational_scope=data["operational_scope"],
        environment=data["environment"],

        modules=data.get("modules", []),
        adapters=data.get("adapters", []),

        previous_scenarios=data.get("previous_scenarios", []),
        next_scenarios=data.get("next_scenarios", []),

        diagrams=data.get("diagrams", []),

        diagram_profiles=data.get(
            "diagram_profiles",
            []
        ),

        readme_template=data.get(
            "readme_template",
            ""
        )
    )
