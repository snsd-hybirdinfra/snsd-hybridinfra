from dataclasses import dataclass, field
from typing import List


@dataclass
class RelationshipGraph:
    scenario_name: str
    lifecycle_level: str

    upstream: List[str] = field(default_factory=list)
    downstream: List[str] = field(default_factory=list)

    related_visibility: List[str] = field(default_factory=list)
    related_correlation: List[str] = field(default_factory=list)
    related_recovery: List[str] = field(default_factory=list)
    related_resilience: List[str] = field(default_factory=list)
    related_continuity: List[str] = field(default_factory=list)

    modules: List[str] = field(default_factory=list)
    adapters: List[str] = field(default_factory=list)
