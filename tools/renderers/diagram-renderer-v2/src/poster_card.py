from src.text_utils import escape_xml
from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, status_color


def render_card(
    card: dict,
    x: int,
    y: int,
    width: int,
    height: int
):

    title = escape_xml(
        card.get(
            "title",
            ""
        )
    )

    subtitle = escape_xml(
        card.get(
            "subtitle",
            ""
        )
    )

    card_type = escape_xml(
        card.get(
            "type",
            ""
        )
    )

    status = escape_xml(
        card.get(
            "status",
            ""
        )
    )

    icon = escape_xml(
        card.get(
            "icon",
            "■"
        )
    )

    color = status_color(
        card.get(
            "status",
            ""
        )
    )

    return [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="22" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<circle cx="{x + 42}" cy="{y + 42}" r="24" '
        f'fill="#020617" stroke="{color}" stroke-width="2" />',

        f'<text x="{x + 42}" y="{y + 51}" '
        f'font-size="24" text-anchor="middle">'
        f'{icon}</text>',

        f'<text x="{x + 82}" y="{y + 34}" '
        f'fill="{TEXT_PRIMARY}" font-size="20" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 82}" y="{y + 62}" '
        f'fill="{TEXT_SECONDARY}" font-size="14">'
        f'{subtitle}</text>',

        f'<text x="{x + 82}" y="{y + 90}" '
        f'fill="{TEXT_MUTED}" font-size="13">'
        f'{card_type}</text>',

        f'<rect x="{x + width - 130}" y="{y + height - 42}" '
        f'width="104" height="26" rx="13" '
        f'fill="#020617" stroke="{color}" stroke-width="1" />',

        f'<text x="{x + width - 78}" y="{y + height - 24}" '
        f'fill="{color}" font-size="12" text-anchor="middle" font-weight="bold">'
        f'{status}</text>'
    ]
