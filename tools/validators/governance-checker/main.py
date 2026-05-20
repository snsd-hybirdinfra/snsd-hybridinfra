import yaml

from pathlib import Path
from jsonschema import validate


REPO_ROOT = Path(__file__).resolve().parents[3]


SCHEMA_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "schemas"
    / "governance"
    / "governance-contract.schema.yaml"
)

RULE_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "schemas"
    / "governance"
    / "governance-rules.yaml"
)


def load_yaml(path: Path):

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
        "Shared governance validation passed."
    )

    print(
        f"Required sections: {rules['required_sections']}"
    )

    print(
        f"Lifecycle flow: {rules['lifecycle_flow']}"
    )

    print(
        f"Diagram policy: {rules['diagram_policy']}"
    )


if __name__ == "__main__":
    main()
