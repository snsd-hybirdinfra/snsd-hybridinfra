from jinja2 import Environment
from jinja2 import FileSystemLoader


def render_template(
    template_dir: str,
    template_name: str,
    context: dict
):

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    template = env.get_template(
        template_name
    )

    return template.render(**context)
