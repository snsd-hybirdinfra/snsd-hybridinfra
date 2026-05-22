from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

STATE_MODEL_PATH = (
    REPO_ROOT
    / "tools"
    / "orchestration-runtime"
    / "configs"
    / "execution-state-model.yaml"
)


def load_execution_state_model():

    with open(
        STATE_MODEL_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)
