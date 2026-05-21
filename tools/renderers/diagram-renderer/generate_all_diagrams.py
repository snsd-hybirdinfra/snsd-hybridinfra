from pathlib import Path
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[2]

RENDERER = (
    REPO_ROOT
    / "tools"
    / "renderers"
    / "diagram-renderer"
    / "main.py"
)

PYTHON = (
    REPO_ROOT
    / "tools"
    / "renderers"
    / "diagram-renderer"
    / "venv"
    / "Scripts"
    / "python.exe"
)


def discover_specs():

    return sorted(
        REPO_ROOT.rglob(
            "*.spec.yaml"
        )
    )


def render_spec(spec_path: Path):

    print(
        f"[RENDER] {spec_path}"
    )

    subprocess.run(
        [
            str(PYTHON),
            str(RENDERER),
            str(spec_path)
        ],
        check=True
    )


def main():

    specs = discover_specs()

    print(
        f"Discovered specs: {len(specs)}"
    )

    for spec in specs:

        render_spec(
            spec
        )

    print(
        "Bulk diagram generation completed."
    )


if __name__ == "__main__":
    main()
