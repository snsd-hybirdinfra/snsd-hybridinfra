from dataclasses import dataclass


@dataclass
class AdapterMetadata:
    adapter_name: str
    integration_type: str
    target_platform: str
