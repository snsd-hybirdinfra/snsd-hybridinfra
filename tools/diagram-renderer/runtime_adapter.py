from pathlib import Path

from main import load_yaml, write_svg
from src.poster_builder import build_poster_svg


def render_poster(
    input_path: str,
    output_path: str | None = None
) -> str:
    yaml_path = Path(input_path).resolve()

    if not yaml_path.exists():
        raise FileNotFoundError(
            f"Poster YAML not found: {yaml_path}"
        )

    data = load_yaml(
        yaml_path
    )

    svg = build_poster_svg(
        data
    )

    if output_path:
        svg_path = Path(output_path).resolve()
    else:
        svg_path = yaml_path.with_suffix(
            ".svg"
        )

    write_svg(
        svg_path,
        svg
    )

    return str(
        svg_path
    )


def render_many(
    input_paths: list[str]
) -> list[str]:
    outputs = []

    for input_path in input_paths:
        outputs.append(
            render_poster(
                input_path
            )
        )

    return outputs

