import yaml
from pathlib import Path


def load_yaml(path: str) -> dict:

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"YAML file not found: {path}"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if data is None:
        raise ValueError(
            f"YAML file is empty or invalid: {path}"
        )

    return data
