from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parents[3]
        / "tools"
    )
)

from shared_runtime.src.runtime_encoding import (
    configure_runtime_encoding
)

configure_runtime_encoding()
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

