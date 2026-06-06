from src.text_utils import escape_truncated
from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_MUTED


LEGEND_COLOR_MAP = {
    "blue": "#2563eb",
    "purple": "#7c3aed",
    "cyan": "#0891b2",
    "green": "#16a34a",
    "red": "#dc2626",
    "orange": "#f97316",
    "yellow": "#eab308",
    "gray": "#64748b"
}


def normalize_legend_items(
    data: dict
):

    legend = data.get(
        "legend",
        []
    )

    if isinstance(
        legend,
        dict
    ):

        legend = [
            legend
        ]

    items = []

    for item in legend:

        if isinstance(
            item,
            dict
        ):

            items.append(
                item
            )

    return items[:8]


def resolve_color(
    value
):

    if not value:

        return "#64748b"

    text = str(
        value
    )

    if text.startswith(
        "#"
    ):

        return text

    return LEGEND_COLOR_MAP.get(
        text.lower(),
        "#64748b"
    )


def render_legend(
    data: dict,
    layout: dict
):

    legend_layout = layout.get(
        "legend",
        layout
    )

    x = legend_layout["x"]
    y = legend_layout["y"]
    width = legend_layout["width"]
    height = legend_layout["height"]

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="26" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 28}" y="{y + 42}" '
        f'fill="{TEXT_PRIMARY}" font-size="22" font-weight="bold">'
        f'Legend</text>',

        f'<text x="{x + 28}" y="{y + 70}" '
        f'fill="{TEXT_MUTED}" font-size="13">'
        f'Operational role and visual mapping</text>'
    ]

    items = normalize_legend_items(
        data
    )

    item_y = y + 112

    for index, item in enumerate(
        items
    ):

        current_y = item_y + index * 34

        label = escape_truncated(
            item.get(
                "label",
                ""
            ),
            32
        )

        color = resolve_color(
            item.get(
                "color",
                ""
            )
        )

        elements.extend(
            [
                f'<circle cx="{x + 42}" cy="{current_y - 5}" r="8" '
                f'fill="{color}" />',

                f'<text x="{x + 64}" y="{current_y}" '
                f'fill="{TEXT_MUTED}" font-size="13" font-weight="bold">'
                f'{label}</text>'
            ]
        )

    return elements


