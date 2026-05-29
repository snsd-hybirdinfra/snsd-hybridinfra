import sys
from pathlib import Path

import yaml

CURRENT_DIR = Path(
    __file__
).resolve().parent

if str(
    CURRENT_DIR
) not in sys.path:

    sys.path.insert(
        0,
        str(
            CURRENT_DIR
        )
    )

from src.poster_builder import build_poster_svg


def load_yaml(
    path: Path
):

    with path.open(
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(
            file
        )


def main():

    if len(
        sys.argv
    ) < 2:

        print(
            "Usage: python main.py <poster-yaml>"
        )

        sys.exit(
            1
        )

    input_path = Path(
        sys.argv[1]
    )

    if not input_path.exists():

        print(
            f"Input file not found: {input_path}"
        )

        sys.exit(
            1
        )

    data = load_yaml(
        input_path
    )

    svg = build_poster_svg(
        data
    )

    output_path = input_path.with_suffix(
        ".svg"
    )

    output_path.write_text(
        svg,
        encoding="utf-8"
    )

    print(
        f"Generated: {output_path}"
    )


if __name__ == "__main__":

    main()
