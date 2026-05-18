from dataclasses import dataclass, field
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

    readme_template: str = ""
