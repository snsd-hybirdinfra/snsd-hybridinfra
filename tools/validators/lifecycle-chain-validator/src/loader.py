from pathlib import Path
import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]

SCENARIOS_ROOT = (
    REPO_ROOT
    / "scenarios"
)

RULE_PATH = (
    REPO_ROOT
    / "tools"
    / "validators"
    / "lifecycle-chain-validator"
    / "rules"
    / "lifecycle-chain-rules.yaml"
)


def load_yaml(
    path: Path
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def load_rules():

    return load_yaml(
        RULE_PATH
    )


def discover_scenario_readmes():

    return sorted(
        SCENARIOS_ROOT.glob(
            "level-*/*/README.md"
        )
    )
