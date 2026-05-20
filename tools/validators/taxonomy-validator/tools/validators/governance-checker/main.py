import yaml

from jsonschema import validate


SCHEMA_PATH = (
    "schemas/governance-schema.yaml"
)

RULE_PATH = (
    "examples/governance-rules.yaml"
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
        "Governance validation passed."
    )

    print(
        f"Required sections: {rules['required_sections']}"
    )

    print(
        f"Lifecycle flow: {rules['required_lifecycle_flow']}"
    )

    print(
        f"Diagram policy: {rules['required_diagram_policy']}"
    )


if __name__ == "__main__":
    main()
