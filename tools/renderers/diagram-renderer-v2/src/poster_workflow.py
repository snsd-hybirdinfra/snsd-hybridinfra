from src.text_utils import escape_xml
from src.poster_theme import PANEL_ALT, PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, status_color


def render_workflow(
    workflow: dict,
    layout: dict
):

    x = layout["workflow"]["x"]
    y = layout["workflow"]["y"]
    width = layout["workflow"]["width"]
    height = layout["workflow"]["height"]

    title = escape_xml(
        workflow.get(
            "title",
            "Operational Workflow"
        )
    )

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="30" fill="{PANEL_ALT}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 34}" y="{y + 48}" '
        f'fill="{TEXT_PRIMARY}" font-size="26" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 34}" y="{y + 78}" '
        f'fill="{TEXT_MUTED}" font-size="15">'
        f'Visibility lifecycle execution rail</text>'
    ]

    steps = workflow.get(
        "steps",
        []
    )

    step_x = x + 42
    step_y = y + 125
    step_width = width - 84
    step_height = 118
    step_gap = 38

    line_x = x + 72

    if steps:

        elements.append(
            f'<line x1="{line_x}" y1="{step_y + 36}" '
            f'x2="{line_x}" y2="{step_y + (len(steps) - 1) * (step_height + step_gap) + 36}" '
            f'stroke="#475569" stroke-width="3" stroke-linecap="round" />'
        )

    for index, step in enumerate(
        steps
    ):

        current_y = step_y + index * (
            step_height + step_gap
        )

        status = step.get(
            "status",
            ""
        )

        color = status_color(
            status
        )

        step_title = escape_xml(
            step.get(
                "title",
                ""
            )
        )

        description = escape_xml(
            step.get(
                "description",
                ""
            )
        )

        safe_status = escape_xml(
            status
        )

        elements.extend(
            [
                f'<circle cx="{line_x}" cy="{current_y + 36}" r="20" '
                f'fill="#020617" stroke="{color}" stroke-width="3" />',

                f'<text x="{line_x}" y="{current_y + 43}" '
                f'fill="{color}" font-size="17" text-anchor="middle" font-weight="bold">'
                f'{index + 1}</text>',

                f'<rect x="{step_x + 58}" y="{current_y}" '
                f'width="{step_width - 58}" height="{step_height}" '
                f'rx="22" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

                f'<text x="{step_x + 84}" y="{current_y + 36}" '
                f'fill="{TEXT_PRIMARY}" font-size="21" font-weight="bold">'
                f'{step_title}</text>',

                f'<text x="{step_x + 84}" y="{current_y + 66}" '
                f'fill="{TEXT_SECONDARY}" font-size="13">'
                f'{description}</text>',

                f'<rect x="{step_x + 84}" y="{current_y + 82}" '
                f'width="112" height="24" rx="12" '
                f'fill="#020617" stroke="{color}" stroke-width="1" />',

                f'<text x="{step_x + 140}" y="{current_y + 99}" '
                f'fill="{color}" font-size="11" text-anchor="middle" font-weight="bold">'
                f'{safe_status}</text>'
            ]
        )

    return elements
