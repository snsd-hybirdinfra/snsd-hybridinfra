from pathlib import Path
import subprocess


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

VALIDATORS = [

    "capability-validator",
    "adjacency-validator",
    "qualification-validator",
    "complexity-validator"
]


def run_validator(
    validator_name: str
):

    validator_main = (

        REPO_ROOT

        / "tools"
        / "validators"
        / validator_name
        / "main.py"
    )

    print(
        f"Running validator: "
        f"{validator_name}"
    )

    result = subprocess.run(

        [
            "python",
            str(validator_main)
        ],

        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print(result.stderr)

        raise RuntimeError(
            f"Validator failed: "
            f"{validator_name}"
        )

    print(result.stdout)


def main():

    for validator in VALIDATORS:

        run_validator(
            validator
        )

    print(
        "Scenario governance validation complete."
    )


if __name__ == "__main__":
    main()
