from pathlib import Path
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

RULE_PATH = (
    REPO_ROOT
    / "governance"
    / "scenario-adjacency-rules.yaml"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def validate_transition(
    previous_level: str,
    current_level: str,
    rules: dict
):

    adjacency = rules[
        "lifecycle_adjacency_rules"
    ]

    current_rules = adjacency[
        previous_level
    ]

    allowed_next = current_rules.get(
        "allowed_next",
        []
    )

    if current_level not in allowed_next:

        raise ValueError(
            f"Invalid lifecycle transition: "
            f"{previous_level} -> "
            f"{current_level}"
        )

    print(
        f"Validated transition: "
        f"{previous_level} -> "
        f"{current_level}"
    )


def main():

    rules = load_yaml(
        RULE_PATH
    )

    validate_transition(
        "level-2-correlation",
        "level-3-recovery",
        rules
    )


if __name__ == "__main__":
    main()
