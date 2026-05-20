from pathlib import Path
import subprocess


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

BULK_INPUT_DIR = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
    / "bulk-inputs"
)

SCENARIO_GENERATOR_DIR = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
)

SCENARIO_GENERATOR_MAIN = (
    SCENARIO_GENERATOR_DIR
    / "main.py"
)


def collect_yaml_files():

    return sorted(
        BULK_INPUT_DIR.glob("*.yaml")
    )


def run_generator(
    yaml_file: Path
):

    print(
        f"Generating scenario: "
        f"{yaml_file.name}"
    )

    result = subprocess.run(

        [
            "python",
            str(SCENARIO_GENERATOR_MAIN),
            str(yaml_file)
        ],

        cwd=SCENARIO_GENERATOR_DIR,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print(result.stderr)

        raise RuntimeError(
            f"Generation failed: "
            f"{yaml_file.name}"
        )

    print(result.stdout)


def main():

    yaml_files = collect_yaml_files()

    print(
        f"Bulk scenario count: "
        f"{len(yaml_files)}"
    )

    for yaml_file in yaml_files:

        run_generator(
            yaml_file
        )

    print(
        "Bulk scenario generation complete."
    )


if __name__ == "__main__":
    main()
