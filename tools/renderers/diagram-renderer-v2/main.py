from pathlib import Path
import sys
import yaml

from src.schema_validator import (
    validate_schema
)

from src.layout_profile import (
    resolve_layout_profile
)

from src.svg_builder import (
    build_svg
)


def main():

    if len(sys.argv) < 2:

        raise ValueError(
            "Usage: python main.py <example.yaml>"
        )

    example = Path(
        sys.argv[1]
    )

    data = yaml.safe_load(
        example.read_text(
            encoding="utf-8"
        )
    )

    validate_schema(
        data
    )

    profile = resolve_layout_profile(
        data["diagram"]["lifecycle"]
    )

    print(
        f"Resolved layout profile: {profile}"
    )

    svg = build_svg(
        data,
        profile
    )

    output = (
        example.parent
        / f'{example.stem}.svg'
    )

    output.write_text(
        svg,
        encoding="utf-8"
    )

    print(
        f"Generated: {output}"
    )


if __name__ == "__main__":
    main()

