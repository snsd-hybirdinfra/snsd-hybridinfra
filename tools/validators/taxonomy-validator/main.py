import yaml

from pathlib import Path
from jsonschema import validate


SCHEMA_PATH = (
    "schemas/taxonomy-schema.yaml"
)

RULE_PATH = (
    "examples/taxonomy-rules.yaml"
)


def load_yaml(path: str):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def main():

    schema = load_yaml(
        SCHEMA_PATH
    )

    rules = load_yaml(
        RULE_PATH
    )

    validate(
        instance=rules,
        schema=schema
    )

    print(
        "Taxonomy validation passed."
    )

    print(
        f"Lifecycle levels: {rules['lifecycle_levels']}"
    )

    print(
        f"Module pattern: {rules['module_name_pattern']}"
    )

    print(
        f"Adapter pattern: {rules['adapter_name_pattern']}"
    )


if __name__ == "__main__":
    main()
