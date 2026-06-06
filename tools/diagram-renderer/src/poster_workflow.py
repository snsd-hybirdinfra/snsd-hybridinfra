from src.text_utils import escape_truncated
from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, status_color


def render_workflow(
    data: dict,
    layout: dict
):

    workflow_layout = layout.get(
        "workflow",
        layout
    )

    x = workflow_layout["x"]
    y = workflow_layout["y"]
    width = workflow_layout["width"]
    height = workflow_layout["height"]

    workflow = data.get(
        "workflow",
        {}
    )

    if not isinstance(
        workflow,
        dict
    ):

        workflow = {}

    title = escape_truncated(
        workflow.get(
            "title",
            "Operational Workflow"
        ),
        34
    )

    steps = workflow.get(
        "steps",
        []
    )

    if not isinstance(
        steps,
        list
    ):

        steps = []

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="28" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 30}" y="{y + 44}" '
        f'fill="{TEXT_PRIMARY}" font-size="24" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 30}" y="{y + 74}" '
        f'fill="{TEXT_SECONDARY}" font-size="13">'
        f'Lifecycle execution sequence</text>'
    ]

    start_y = y + 120
    step_gap = 116 if len(steps) <= 5 else 92

    for index, step in enumerate(
        steps[:6]
    ):

        if not isinstance(
            step,
            dict
        ):

            continue

        step_y = start_y + index * step_gap

        title_text = escape_truncated(
            step.get(
                "title",
                ""
            ),
            24
        )

        description = escape_truncated(
            step.get(
                "description",
                ""
            ),
            46
        )

        status = step.get(
            "status",
            ""
        )

        color = status_color(
            status
        )

        elements.extend(
            [
                f'<circle cx="{x + 54}" cy="{step_y}" r="18" '
                f'fill="{color}" stroke="{color}" stroke-width="3" opacity="0.95" />',

                f'<text x="{x + 54}" y="{step_y + 6}" '
                f'fill="#020617" font-size="13" text-anchor="middle" font-weight="bold">'
                f'{index + 1}</text>',

                f'<text x="{x + 88}" y="{step_y - 4}" '
                f'fill="{TEXT_PRIMARY}" font-size="17" font-weight="bold">'
                f'{title_text}</text>',

                f'<text x="{x + 88}" y="{step_y + 20}" '
                f'fill="{TEXT_MUTED}" font-size="12">'
                f'{description}</text>',

                f'<rect x="{x + width - 128}" y="{step_y - 18}" '
                f'width="96" height="26" rx="13" '
                f'fill="#020617" stroke="{color}" stroke-width="1" />',

                f'<text x="{x + width - 80}" y="{step_y}" '
                f'fill="{color}" font-size="10" text-anchor="middle" font-weight="bold">'
                f'{escape_truncated(status, 11)}</text>'
            ]
        )

        if index < len(
            steps[:6]
        ) - 1:

            elements.append(
                f'<line x1="{x + 54}" y1="{step_y + 22}" '
                f'x2="{x + 54}" y2="{step_y + step_gap - 24}" '
                f'stroke="#475569" stroke-width="2" stroke-dasharray="6 6" opacity="0.7" />'
            )

    return elements


