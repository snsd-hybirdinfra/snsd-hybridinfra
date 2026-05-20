from pathlib import Path
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

MODEL_PATH = (
    REPO_ROOT
    / "governance"
    / "scenario-qualification-model.yaml"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def validate_qualification(
    qualification: str,
    model: dict
):

    levels = model[
        "scenario_qualification_levels"
    ]

    if qualification not in levels:

        raise ValueError(
            f"Unknown qualification level: "
            f"{qualification}"
        )

    info = levels[
        qualification
    ]

    print(
        f"Qualification: "
        f"{qualification}"
    )

    print(
        f"Description: "
        f"{info['description']}"
    )

    print(
        "Requirements:"
    )

    for requirement in info[
        "requirements"
    ]:

        print(
            f"- {requirement}"
        )


def main():

    model = load_yaml(
        MODEL_PATH
    )

    validate_qualification(
        "gold-reference",
        model
    )


if __name__ == "__main__":
    main()
