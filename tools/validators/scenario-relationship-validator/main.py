from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

EXAMPLES_ROOT = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
    / "examples"
)


ALLOWED_NEXT = {
    "level-1-visibility": "level-2-correlation",
    "level-2-correlation": "level-3-recovery",
    "level-3-recovery": "level-4-resilience",
    "level-4-resilience": "level-5-continuity"
}


ALLOWED_PREVIOUS = {
    "level-2-correlation": "level-1-visibility",
    "level-3-recovery": "level-2-correlation",
    "level-4-resilience": "level-3-recovery",
    "level-5-continuity": "level-4-resilience"
}


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def infer_lifecycle_from_path(value: str):

    parts = value.split("/")

    for part in parts:

        if part.startswith("level-"):

            return part

    return None


def validate_next_relationship(
    scenario_path: Path,
    lifecycle: str,
    relationships: dict
):

    next_scenario = relationships.get(
        "next_lifecycle_scenario"
    )

    if not next_scenario:

        return

    expected = ALLOWED_NEXT.get(
        lifecycle
    )

    actual = infer_lifecycle_from_path(
        next_scenario
    )

    if actual != expected:

        raise ValueError(
            f"Invalid next lifecycle relationship in {scenario_path}: "
            f"{lifecycle} must point to {expected}, got {actual}"
        )


def validate_previous_relationship(
    scenario_path: Path,
    lifecycle: str,
    relationships: dict
):

    previous_scenario = relationships.get(
        "previous_lifecycle_scenario"
    )

    if not previous_scenario:

        return

    expected = ALLOWED_PREVIOUS.get(
        lifecycle
    )

    actual = infer_lifecycle_from_path(
        previous_scenario
    )

    if actual != expected:

        raise ValueError(
            f"Invalid previous lifecycle relationship in {scenario_path}: "
            f"{lifecycle} must point to {expected}, got {actual}"
        )


def validate_convergence_rules(
    scenario_path: Path,
    lifecycle: str,
    relationships: dict
):

    if (
        "convergence_parent" in relationships
        and lifecycle != "level-5-continuity"
    ):

        raise ValueError(
            f"Invalid convergence_parent in {scenario_path}: "
            f"only level-5-continuity may declare convergence_parent"
        )

    if (
        "convergence_children" in relationships
        and lifecycle != "level-4-resilience"
    ):

        raise ValueError(
            f"Invalid convergence_children in {scenario_path}: "
            f"only level-4-resilience may declare convergence_children"
        )

    if (
        "continuity_reference" in relationships
        and lifecycle != "level-4-resilience"
    ):

        raise ValueError(
            f"Invalid continuity_reference in {scenario_path}: "
            f"only level-4-resilience may declare continuity_reference"
        )


def validate_relationships(
    scenario_path: Path
):

    data = load_yaml(
        scenario_path
    )

    lifecycle = data.get(
        "lifecycle_level"
    )

    relationships = data.get(
        "relationships",
        {}
    )

    validate_next_relationship(
        scenario_path,
        lifecycle,
        relationships
    )

    validate_previous_relationship(
        scenario_path,
        lifecycle,
        relationships
    )

    validate_convergence_rules(
        scenario_path,
        lifecycle,
        relationships
    )


def main():

    scenario_files = sorted(
        EXAMPLES_ROOT.glob(
            "*.yaml"
        )
    )

    checked = 0

    for scenario_file in scenario_files:

        validate_relationships(
            scenario_file
        )

        checked += 1

    print(
        f"Scenario relationship validation passed. "
        f"Scenario metadata files checked: {checked}"
    )


if __name__ == "__main__":
    main()
