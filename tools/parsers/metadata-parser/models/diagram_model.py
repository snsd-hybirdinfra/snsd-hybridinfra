from dataclasses import dataclass, field
from typing import List


@dataclass
class DiagramModel:
    scenario_name: str
    lifecycle_level: str
    title: str
    diagram_type: str

    modules: List[str] = field(default_factory=list)
    adapters: List[str] = field(default_factory=list)
    workflow_steps: List[str] = field(default_factory=list)

    output_name: str = ""
