from pathlib import Path
import subprocess


def run_diagram_renderer():

    repo_root = Path(__file__).resolve().parents[4]

    renderer_path = (
        repo_root
        / "tools"
        / "renderers"
        / "diagram-renderer"
    )

    python_path = (
        renderer_path
        / "venv"
        / "Scripts"
        / "python.exe"
    )

    main_path = renderer_path / "main.py"

    if not renderer_path.exists():
        raise FileNotFoundError(
            f"Diagram renderer path not found: {renderer_path}"
        )

    if not python_path.exists():
        raise FileNotFoundError(
            f"Diagram renderer venv python not found: {python_path}"
        )

    if not main_path.exists():
        raise FileNotFoundError(
            f"Diagram renderer main.py not found: {main_path}"
        )

    result = subprocess.run(
        [str(python_path), str(main_path)],
        cwd=str(renderer_path),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout
