from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

CONTRACT_PATH = (
    REPO_ROOT
    / "tools"
    / "orchestration-runtime"
    / "configs"
    / "artifact-contracts.yaml"
)

SCENARIOS_ROOT = (
    REPO_ROOT
    / "scenarios"
)


CANONICAL_SCENARIOS = [
    "vpn-connectivity-monitoring",
    "vpn-latency-correlation",
    "vpn-tunnel-recovery-automation",
    "multi-site-routing-failover",
    "enterprise-network-continuity"
]


REQUIRED_DIAGRAMS = [
    "architecture-overview.png",
    "workflow-overview.png",
    "relationship-overview.png"
]


REQUIRED_SPECS = [
    "architecture-overview.spec.yaml",
    "workflow-overview.spec.yaml",
    "relationship-overview.spec.yaml"
]


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def validate_scenario_package(
    scenario_path: Path
):

    required_directories = [
        "diagrams",
        "evidence",
        "artifacts",
        "architecture",
        "implementation"
    ]

    for directory in required_directories:

        path = scenario_path / directory

        if not path.exists():

            raise FileNotFoundError(
                f"Missing required directory: {path}"
            )

    readme_path = (
        scenario_path
        / "README.md"
    )

    if not readme_path.exists():

        raise FileNotFoundError(
            f"Missing README: {readme_path}"
        )


def validate_diagram_artifacts(
    scenario_path: Path
):

    diagrams_path = (
        scenario_path
        / "diagrams"
    )

    for diagram in REQUIRED_DIAGRAMS:

        path = diagrams_path / diagram

        if not path.exists():

            raise FileNotFoundError(
                f"Missing diagram artifact: {path}"
            )

    for spec in REQUIRED_SPECS:

        path = diagrams_path / spec

        if not path.exists():

            raise FileNotFoundError(
                f"Missing diagram spec: {path}"
            )


def validate_scenarios():

    lifecycle_directories = sorted(
        SCENARIOS_ROOT.glob(
            "level-*"
        )
    )

    checked = 0

    for lifecycle in lifecycle_directories:

        scenario_directories = sorted(
            lifecycle.iterdir()
        )

        for scenario in scenario_directories:

            if not scenario.is_dir():

                continue

            if (
                scenario.name
                not in CANONICAL_SCENARIOS
            ):

                continue

            validate_scenario_package(
                scenario
            )

            validate_diagram_artifacts(
                scenario
            )

            checked += 1

    return checked


def main():

    contracts = load_yaml(
        CONTRACT_PATH
    )

    checked = validate_scenarios()

    print(
        f"Artifact existence validation passed. "
        f"Scenario packages checked: {checked}"
    )

    print(
        f"Loaded artifact contracts: "
        f"{len(contracts.get('artifact_contracts', {}))}"
    )


if __name__ == "__main__":
    main()
