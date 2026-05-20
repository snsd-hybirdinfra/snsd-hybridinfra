from dataclasses import dataclass, field
from typing import Dict
from typing import List


@dataclass
class ScenarioMetadata:
    scenario_name: str
    lifecycle_level: str
    operational_scope: str
    environment: str

    modules: List[str] = field(default_factory=list)
    adapters: List[str] = field(default_factory=list)

    previous_scenarios: List[str] = field(default_factory=list)
    next_scenarios: List[str] = field(default_factory=list)

    diagrams: List[str] = field(default_factory=list)

    diagram_profiles: List[str] = field(default_factory=list)

    diagram_placement: Dict[str, str] = field(
        default_factory=dict
    )

    readme_template: str = ""
