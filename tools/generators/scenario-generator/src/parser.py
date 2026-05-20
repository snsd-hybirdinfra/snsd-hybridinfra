from models.scenario_metadata import ScenarioMetadata

from configs.diagram_profile_mapping import (
    DIAGRAM_PROFILE_MAPPING
)

from configs.diagram_placement_mapping import (
    DIAGRAM_PLACEMENT_MAPPING
)

from src.capability_inference import (
    infer_modules_and_adapters
)


def parse_scenario_metadata(data: dict) -> ScenarioMetadata:

    lifecycle_level = data["lifecycle_level"]

    capabilities = data.get(
        "capabilities",
        []
    )

    inferred = infer_modules_and_adapters(
        capabilities
    )

    default_diagrams = DIAGRAM_PROFILE_MAPPING.get(
        lifecycle_level,
        []
    )

    diagram_profiles = data.get(
        "diagram_profiles",
        default_diagrams
    )

    default_placement = {}

    for diagram in diagram_profiles:

        default_placement[diagram] = (
            DIAGRAM_PLACEMENT_MAPPING.get(
                diagram,
                "section"
            )
        )

    return ScenarioMetadata(

        scenario_name=data["scenario_name"],

        lifecycle_level=lifecycle_level,

        operational_scope=data["operational_scope"],

        environment=data["environment"],

        capabilities=capabilities,

        modules=data.get(
            "modules",
            inferred["modules"]
        ),

        adapters=data.get(
            "adapters",
            inferred["adapters"]
        ),

        previous_scenarios=data.get(
            "previous_scenarios",
            []
        ),

        next_scenarios=data.get(
            "next_scenarios",
            []
        ),

        diagrams=data.get(
            "diagrams",
            diagram_profiles
        ),

        diagram_profiles=diagram_profiles,

        diagram_placement=data.get(
            "diagram_placement",
            default_placement
        ),

        readme_template=data.get(
            "readme_template",
            ""
        )
    )
