from pathlib import Path
import yaml


CONFIG_PATH = (
    Path(__file__)
    .parent.parent
    / "configs"
    / "tool-dependencies.yaml"
)


def load_dependencies():

    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        data = yaml.safe_load(file)

    return data.get(
        "tool_dependencies",
        {}
    )
