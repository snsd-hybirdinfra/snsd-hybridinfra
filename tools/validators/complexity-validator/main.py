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
    / "artificial-complexity-rules.yaml"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def validate_complexity(
    lifecycle_level: str,
    text: str,
    rules: dict
):

    lifecycle_rules = (
        rules[
            "artificial_complexity_rules"
        ][
            "lifecycle_limits"
        ][
            lifecycle_level
        ]
    )

    forbidden_terms = (
        lifecycle_rules.get(
            "forbidden_terms",
            []
        )
    )

    required_terms = (
        lifecycle_rules.get(
            "required_terms",
            []
        )
    )

    normalized_text = text.lower()

    for term in forbidden_terms:

        if term.lower() in normalized_text:

            raise ValueError(
                f"Forbidden complexity term "
                f"detected: {term}"
            )

    for term in required_terms:

        if term.lower() not in normalized_text:

            raise ValueError(
                f"Required resilience term "
                f"missing: {term}"
            )

    print(
        "Artificial complexity validation passed."
    )


def main():

    rules = load_yaml(
        RULE_PATH
    )

    sample_text = '''

    Distributed failover survivability
    validation workflow with resilience
    coordination across multiple sites.

    '''

    validate_complexity(
        "level-4-resilience",
        sample_text,
        rules
    )


if __name__ == "__main__":
    main()
