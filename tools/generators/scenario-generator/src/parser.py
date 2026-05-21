from dataclasses import dataclass
from typing import Optional


@dataclass
class ScenarioMetadata:

    scenario_id: Optional[str]

    scenario_name: str

    scenario_title: Optional[str]

    lifecycle_level: str

    operational_domain: Optional[str]

    operational_pattern: Optional[str]

    capability_tier: Optional[str]

    category: str

    severity: str

    priority: str

    environment: str

    validation_scope: Optional[str]

    telemetry_scope: Optional[str]

    recovery_scope: Optional[str]

    governance_scope: Optional[str]

    description: str

    template_profile: Optional[str]

    diagram_profile: Optional[str]

    validation_profile: Optional[str]

    maturity_profile: Optional[str]

    relationships: Optional[dict]


def parse_scenario_metadata(
    raw_data: dict
):

    return ScenarioMetadata(

        scenario_id=raw_data.get(
            "scenario_id"
        ),

        scenario_name=raw_data[
            "scenario_name"
        ],

        scenario_title=raw_data.get(
            "scenario_title"
        ),

        lifecycle_level=raw_data[
            "lifecycle_level"
        ],

        operational_domain=raw_data.get(
            "operational_domain"
        ),

        operational_pattern=raw_data.get(
            "operational_pattern"
        ),

        capability_tier=raw_data.get(
            "capability_tier"
        ),

        category=raw_data[
            "category"
        ],

        severity=raw_data[
            "severity"
        ],

        priority=raw_data[
            "priority"
        ],

        environment=raw_data[
            "environment"
        ],

        validation_scope=raw_data.get(
            "validation_scope"
        ),

        telemetry_scope=raw_data.get(
            "telemetry_scope"
        ),

        recovery_scope=raw_data.get(
            "recovery_scope"
        ),

        governance_scope=raw_data.get(
            "governance_scope"
        ),

        description=raw_data[
            "description"
        ],

        template_profile=raw_data.get(
            "template_profile"
        ),

        diagram_profile=raw_data.get(
            "diagram_profile"
        ),

        validation_profile=raw_data.get(
            "validation_profile"
        ),

        maturity_profile=raw_data.get(
            "maturity_profile"
        ),

        relationships=raw_data.get(
            "relationships"
        )
    )
