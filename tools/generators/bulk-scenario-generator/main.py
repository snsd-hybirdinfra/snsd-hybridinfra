from pathlib import Path
import csv
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

CATALOG_PATH = (
    REPO_ROOT
    / "governance"
    / "scenario-taxonomy-catalog.csv"
)

OUTPUT_DIR = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "bulk-scenario-generator"
    / "outputs"
)


def load_catalog():

    scenarios = []

    with open(
        CATALOG_PATH,
        "r",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            normalized_row = {
                key.strip(): value
                for key, value in row.items()
            }

            scenarios.append(normalized_row)

    return scenarios


def build_metadata(
    scenario: dict
):

    return {

        "scenario_name":
            scenario["scenario_name"],

        "lifecycle_level":
            scenario["lifecycle_level"],

        "operational_scope":
            scenario["domain"],

        "environment":
            "hybrid-infrastructure",

        "capabilities": [

            scenario[
                "primary_capability"
            ],

            scenario[
                "adjacent_capabilities"
            ]
        ],

        "previous_scenarios": [],

        "next_scenarios": [],

        "diagrams": [
            "topology-architecture"
        ]
    }


def export_yaml(
    metadata: dict
):

    output_path = (
        OUTPUT_DIR
        / f"{metadata['scenario_name']}.yaml"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        yaml.dump(
            metadata,
            file,
            sort_keys=False
        )

    print(
        f"Exported: {output_path.name}"
    )


def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    scenarios = load_catalog()

    print(
        f"Loaded scenarios: "
        f"{len(scenarios)}"
    )

    for scenario in scenarios:

        metadata = build_metadata(
            scenario
        )

        export_yaml(
            metadata
        )


if __name__ == "__main__":
    main()
