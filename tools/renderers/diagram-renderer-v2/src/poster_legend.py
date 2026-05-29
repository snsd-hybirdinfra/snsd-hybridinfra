from src.text_utils import escape_xml
from src.poster_theme import PANEL_ALT, PANEL, BORDER, TEXT_PRIMARY, TEXT_MUTED


LEGEND_COLORS = {
    "blue": "#2563eb",
    "cyan": "#0891b2",
    "green": "#16a34a",
    "yellow": "#ca8a04",
    "red": "#dc2626",
    "purple": "#7c3aed",
    "default": "#64748b"
}


def legend_color(
    color: str
):

    return LEGEND_COLORS.get(
        color,
        LEGEND_COLORS["default"]
    )


def render_legend(
    legend: list,
    layout: dict
):

    box = layout["legend"]

    x = box["x"]
    y = box["y"]
    width = box["width"]
    height = box["height"]

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="30" fill="{PANEL_ALT}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 34}" y="{y + 44}" '
        f'fill="{TEXT_PRIMARY}" font-size="24" font-weight="bold">'
        f'Legend</text>',

        f'<text x="{x + 34}" y="{y + 74}" '
        f'fill="{TEXT_MUTED}" font-size="13">'
        f'Visual semantics</text>'
    ]

    item_x = x + 34
    item_y = y + 96

    for index, item in enumerate(
        legend
    ):

        current_y = item_y + index * 30

        label = escape_xml(
            item.get(
                "label",
                ""
            )
        )

        color = legend_color(
            item.get(
                "color",
                "default"
            )
        )

        elements.extend(
            [
                f'<rect x="{item_x}" y="{current_y - 14}" '
                f'width="22" height="22" rx="6" fill="{color}" />',

                f'<text x="{item_x + 36}" y="{current_y + 3}" '
                f'fill="#cbd5e1" font-size="13">'
                f'{label}</text>'
            ]
        )

    return elements

