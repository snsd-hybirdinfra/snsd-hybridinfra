from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader


REPO_ROOT = Path(__file__).resolve().parents[4]

GENERATOR_ROOT = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
)


def render_template(
    template_root: str,
    template_name: str,
    context: dict
):

    env = Environment(
        loader=FileSystemLoader(
            GENERATOR_ROOT / template_root
        ),
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(
        template_name
    )

    return template.render(
        **context
    )
