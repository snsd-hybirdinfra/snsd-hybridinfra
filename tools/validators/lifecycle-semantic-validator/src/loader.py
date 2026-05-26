from pathlib import Path
import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]

RULE_PATH = (
    REPO_ROOT
    / "tools"
    / "validators"
    / "lifecycle-semantic-validator"
    / "rules"
    / "forbidden-vocabulary.yaml"
)

SCENARIOS_ROOT = (
    REPO_ROOT
    / "scenarios"
)


def load_rules():

    with open(
        RULE_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def discover_readmes():

    return sorted(
        SCENARIOS_ROOT.glob(
            "level-*/*/README.md"
        )
    )
