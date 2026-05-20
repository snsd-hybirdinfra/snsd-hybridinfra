from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Dict


@dataclass
class DiagramModel:

    scenario_name: str
    lifecycle_level: str
    title: str
    diagram_type: str
    output_name: str

    modules: List[str] = field(default_factory=list)
    adapters: List[str] = field(default_factory=list)
    workflow_steps: List[str] = field(default_factory=list)

    topology_nodes: List[Dict] = field(default_factory=list)
    topology_edges: List[Dict] = field(default_factory=list)
