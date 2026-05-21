from pathlib import Path
import sys

from src.spec_renderer import main as render_from_spec


def main():

    if len(sys.argv) < 2:

        raise ValueError(
            "Usage: python main.py <diagram-spec.yaml>"
        )

    render_from_spec()


if __name__ == "__main__":
    main()
