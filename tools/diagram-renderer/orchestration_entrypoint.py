import os
import sys
import shutil
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[1]
SCENARIOS_ROOT = REPO_ROOT / "scenarios"

sys.path.insert(
    0,
    str(ROOT)
)

from src.poster_builder import build_poster_svg
from src.scenario_poster_mapper import map_metadata_to_poster



def load_yaml(
    path: Path
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(
            file
        ) or {}


def write_svg(
    path: Path,
    svg: str
):

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        svg,
        encoding="utf-8"
    )


def find_browser():

    configured_browser = os.environ.get(
        "POSTER_RENDER_BROWSER",
        ""
    ).strip()

    if configured_browser:

        browser_path = Path(
            configured_browser
        )

        if browser_path.exists():

            return str(
                browser_path
            )

    candidates = [
        shutil.which("msedge"),
        shutil.which("chrome"),
        shutil.which("chrome.exe"),
        shutil.which("msedge.exe"),
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for candidate in candidates:

        if candidate and Path(candidate).exists():

            return str(
                candidate
            )

    raise RuntimeError(
        "No supported browser found for SVG to PNG export. "
        "Install Microsoft Edge or Chrome, or set POSTER_RENDER_BROWSER."
    )


def convert_svg_to_png(
    svg_path: Path,
    png_path: Path
):

    browser = find_browser()

    png_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    profile_dir = (
        REPO_ROOT
        / "runtime-workspace"
        / "browser-profiles"
        / svg_path.parent.parent.name
    )

    if profile_dir.exists():
        shutil.rmtree(profile_dir, ignore_errors=True)

    profile_dir.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-popup-blocking",
            "--disable-notifications",
            "--no-first-run",
            "--no-default-browser-check",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--high-dpi-support=1",
            "--font-render-hinting=none",
            "--window-size=2600,1900",
            f"--user-data-dir={profile_dir}",
            f"--screenshot={png_path}",
            svg_path.resolve().as_uri()
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120
    )

    shutil.rmtree(profile_dir, ignore_errors=True)

    if result.returncode != 0:

        raise RuntimeError(
            "Browser PNG export failed.\n"
            + result.stdout
            + "\n"
            + result.stderr
        )

    if not png_path.exists():

        raise RuntimeError(
            f"PNG was not generated: {png_path}"
        )

    if png_path.stat().st_size < 1000:

        raise RuntimeError(
            f"PNG output is too small: {png_path}"
        )


def discover_example_inputs():

    examples_dir = ROOT / "examples"

    return sorted(
        examples_dir.glob(
            "*.yaml"
        )
    )


def discover_scenario_inputs():

    configured_inputs = os.environ.get(
        "POSTER_RENDER_INPUTS",
        ""
    ).strip()

    if configured_inputs:

        return [
            Path(
                item.strip()
            ).resolve()
            for item in configured_inputs.split(
                ";"
            )
            if item.strip()
        ]

    return sorted(
        SCENARIOS_ROOT.glob(
            "*/*/metadata.yaml"
        )
    )


def resolve_example_output_paths(
    input_path: Path,
    workspace: Path
):

    output_dir = workspace

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    svg_path = output_dir / input_path.with_suffix(
        ".svg"
    ).name

    png_path = output_dir / input_path.with_suffix(
        ".png"
    ).name

    return svg_path, png_path


def resolve_scenario_output_paths(
    metadata_path: Path
):

    diagrams_dir = metadata_path.parent / "diagrams"

    diagrams_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    svg_path = diagrams_dir / "operational-poster.svg"
    png_path = diagrams_dir / "operational-poster.png"

    return svg_path, png_path


def render_example(
    input_path: Path,
    workspace: Path
):

    data = load_yaml(
        input_path
    )

    svg = build_poster_svg(
        data
    )

    svg_path, png_path = resolve_example_output_paths(
        input_path,
        workspace
    )

    write_svg(
        svg_path,
        svg
    )

    convert_svg_to_png(
        svg_path,
        png_path
    )

    print(
        f"[OK] Rendered example SVG: {svg_path}"
    )

    print(
        f"[OK] Rendered example PNG: {png_path}"
    )

    return {
        "svg": svg_path,
        "png": png_path
    }


def render_scenario(
    metadata_path: Path
):

    scenario_dir = metadata_path.parent
    poster_yaml = scenario_dir / "poster.yaml"

    if poster_yaml.exists():

        print(
            f"[INFO] Using poster.yaml: {poster_yaml}"
        )

        poster_data = load_yaml(
            poster_yaml
        )

        input_source = poster_yaml

    else:

        print(
            f"[INFO] Using metadata fallback: {metadata_path}"
        )

        metadata = load_yaml(
            metadata_path
        )

        poster_data = map_metadata_to_poster(
            metadata
        )

        input_source = metadata_path

    svg = build_poster_svg(
        poster_data
    )

    svg_path, png_path = resolve_scenario_output_paths(
        metadata_path
    )

    write_svg(
        svg_path,
        svg
    )

    convert_svg_to_png(
        svg_path,
        png_path
    )

    print(
        f"[OK] Rendered scenario SVG: {svg_path}"
    )

    print(
        f"[OK] Rendered scenario PNG: {png_path}"
    )

    return {
        "source": input_source,
        "svg": svg_path,
        "png": png_path
    }

def validate_artifact(
    path: Path,
    artifact_type: str
):

    if not path.exists():

        raise RuntimeError(
            f"{artifact_type} was not generated: {path}"
        )

    if path.stat().st_size < 1000:

        raise RuntimeError(
            f"{artifact_type} output is too small: {path}"
        )


def main():

    run_id = os.environ.get(
        "RUN_ID",
        "manual"
    )

    mode = os.environ.get(
        "POSTER_RENDER_MODE",
        "scenarios"
    ).strip().lower()

    workspace = Path(
        os.environ.get(
            "TOOL_WORKSPACE",
            ROOT / "outputs" / run_id
        )
    ).resolve()

    workspace.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"[INFO] diagram-renderer run_id={run_id}"
    )

    print(
        f"[INFO] mode={mode}"
    )

    print(
        f"[INFO] workspace={workspace}"
    )

    rendered = []

    if mode == "examples":

        input_files = discover_example_inputs()

        if not input_files:

            raise RuntimeError(
                "No poster example YAML inputs found."
            )

        for input_path in input_files:

            result = render_example(
                input_path,
                workspace
            )

            validate_artifact(
                result["svg"],
                "SVG"
            )

            validate_artifact(
                result["png"],
                "PNG"
            )

            rendered.append(
                result
            )

    else:

        input_files = discover_scenario_inputs()

        if not input_files:

            raise RuntimeError(
                "No scenario metadata.yaml inputs found."
            )

        for metadata_path in input_files:

            result = render_scenario(
                metadata_path
            )

            validate_artifact(
                result["svg"],
                "SVG"
            )

            validate_artifact(
                result["png"],
                "PNG"
            )

            rendered.append(
                result
            )

    manifest_path = workspace / "diagram-renderer-artifacts.txt"

    artifact_lines = []

    for item in rendered:

        artifact_lines.append(
            str(
                item["svg"]
            )
        )

        artifact_lines.append(
            str(
                item["png"]
            )
        )

    manifest_path.write_text(
        "\n".join(
            artifact_lines
        ),
        encoding="utf-8"
    )

    print(
        f"[OK] Poster artifact manifest: {manifest_path}"
    )

    print(
        f"[OK] Rendered poster count: {len(rendered)}"
    )

    print(
        "[OK] diagram-renderer completed"
    )


if __name__ == "__main__":

    main()









