from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]

PROFILE_PATH = (
    REPO_ROOT
    / "governance"
    / "lifecycle-profiles.yaml"
)


def load_lifecycle_profiles():

    with open(
        PROFILE_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        data = yaml.safe_load(
            file
        )

    return data.get(
        "lifecycle_profiles",
        {}
    )


def resolve_lifecycle_profile(
    lifecycle_level: str
):

    profiles = load_lifecycle_profiles()

    profile = profiles.get(
        lifecycle_level
    )

    if profile is None:

        raise ValueError(
            f"No lifecycle profile registered for: "
            f"{lifecycle_level}"
        )

    return profile
