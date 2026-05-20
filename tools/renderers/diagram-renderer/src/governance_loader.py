import yaml
from pathlib import Path


def load_governance(path: str):

    governance_path = Path(path)

    if not governance_path.exists():
        raise FileNotFoundError(
            f"Governance file not found: {path}"
        )

    with open(
        governance_path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)
