from pathlib import Path
import yaml
from jsonschema import validate


def validate_relationship_graph(data: dict, schema_path: str):
    schema_file = Path(schema_path)

    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    with open(schema_file, "r", encoding="utf-8") as file:
        schema = yaml.safe_load(file)

    validate(instance=data, schema=schema)
    return True
