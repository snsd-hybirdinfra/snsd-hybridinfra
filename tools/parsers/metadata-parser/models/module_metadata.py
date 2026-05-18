from dataclasses import dataclass


@dataclass
class ModuleMetadata:
    module_name: str
    capability_type: str
    operational_role: str
