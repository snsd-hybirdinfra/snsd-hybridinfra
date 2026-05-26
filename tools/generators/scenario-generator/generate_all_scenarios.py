from pathlib import Path
import sys
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[3]

sys.path.append(
    str(
        REPO_ROOT
        / "tools"
    )
)

from shared_runtime.src.runtime_encoding import (
    configure_runtime_encoding
)

configure_runtime_encoding()


GENERATOR_ROOT = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
)

PYTHON = (
    GENERATOR_ROOT
    / "venv"
    / "Scripts"
    / "python.exe"
)

MAIN = (
    GENERATOR_ROOT
    / "main.py"
)

EXAMPLES_ROOT = (
    GENERATOR_ROOT
    / "examples"
)


def discover_examples():

    return sorted(
        EXAMPLES_ROOT.rglob(
            "*.yaml"
        )
    )


def generate_example(
    example_path: Path
):

    print(
        f"[GENERATE] {example_path}"
    )

    subprocess.run(
        [
            str(PYTHON),
            str(MAIN),
            str(example_path)
        ],
        cwd=str(GENERATOR_ROOT),
        check=True,
        encoding="utf-8",
        errors="replace"
    )


def main():

    examples = discover_examples()

    print(
        f"Discovered scenario examples: {len(examples)}"
    )

    for example in examples:

        generate_example(
            example
        )

    print(
        "Scenario batch generation completed."
    )


if __name__ == "__main__":
    main()
