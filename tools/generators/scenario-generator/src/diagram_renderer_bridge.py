from pathlib import Path
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[4]

DIAGRAM_RENDERER_PATH = (
    REPO_ROOT
    / "tools"
    / "renderers"
    / "diagram-renderer"
    / "main.py"
)

DIAGRAM_RENDERER_PYTHON = (
    REPO_ROOT
    / "tools"
    / "renderers"
    / "diagram-renderer"
    / "venv"
    / "Scripts"
    / "python.exe"
)


def render_diagram_spec(
    spec_path: Path
):

    if not DIAGRAM_RENDERER_PYTHON.exists():

        raise FileNotFoundError(
            f"Diagram renderer python not found: "
            f"{DIAGRAM_RENDERER_PYTHON}"
        )

    subprocess.run(
        [
            str(DIAGRAM_RENDERER_PYTHON),
            str(DIAGRAM_RENDERER_PATH),
            str(spec_path)
        ],
        check=True
    )


def render_scenario_diagrams(
    scenario_path: Path
):

    specs = sorted(
        (
            scenario_path
            / "diagrams"
        ).glob(
            "*.spec.yaml"
        )
    )

    for spec_path in specs:

        render_diagram_spec(
            spec_path
        )
