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


def output_paths(
    spec_path: Path
):

    svg_path = (
        spec_path
        .with_suffix("")
        .with_suffix(".svg")
    )

    png_path = svg_path.with_suffix(
        ".png"
    )

    return svg_path, png_path


def should_render(
    spec_path: Path
):

    svg_path, png_path = output_paths(
        spec_path
    )

    if not svg_path.exists():

        return True

    if not png_path.exists():

        return True

    spec_mtime = spec_path.stat().st_mtime
    svg_mtime = svg_path.stat().st_mtime
    png_mtime = png_path.stat().st_mtime

    return (
        spec_mtime > svg_mtime
        or spec_mtime > png_mtime
    )


def render_spec(
    spec_path: Path
):

    print(
        f"[RENDER] {spec_path}"
    )

    subprocess.run(
        [
            str(PYTHON),
            str(RENDERER),
            str(spec_path)
        ],
        check=True,
        encoding="utf-8",
        errors="replace"
    )


def main():

    specs = discover_specs()

    print(
        f"Discovered specs: {len(specs)}"
    )

    rendered = 0
    skipped = 0

    for spec in specs:

        if not should_render(
            spec
        ):

            skipped += 1

            print(
                f"[SKIP] {spec}"
            )

            continue

        render_spec(
            spec
        )

        rendered += 1

    print(
        f"Bulk diagram generation completed. "
        f"Rendered: {rendered}, Skipped: {skipped}"
    )


if __name__ == "__main__":
    main()
