from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader


REPO_ROOT = Path(__file__).resolve().parents[4]

TEMPLATE_ROOT = (
    REPO_ROOT
    / "tools"
    / "generators"
    / "scenario-generator"
    / "templates"
    / "diagrams"
)


env = Environment(
    loader=FileSystemLoader(
        TEMPLATE_ROOT
    ),
    trim_blocks=True,
    lstrip_blocks=True
)


def render_template(
    template_name: str,
    output_path: Path,
    context: dict
):

    template = env.get_template(
        template_name
    )

    rendered = template.render(
        **context
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        rendered,
        encoding="utf-8"
    )

    print(
        f"Generated diagram spec: "
        f"{output_path}"
    )


def generate_level_1_specs(
    scenario_path: Path,
    scenario_name: str
):

    diagrams_path = (
        scenario_path
        / "diagrams"
    )

    context = {
        "scenario_name": scenario_name,
        "lifecycle_level": "level-1-visibility"
    }

    render_template(
        "level-1-architecture.spec.yaml.j2",
        diagrams_path
        / "architecture-overview.spec.yaml",
        context
    )

    render_template(
        "level-1-workflow.spec.yaml.j2",
        diagrams_path
        / "workflow-overview.spec.yaml",
        context
    )
