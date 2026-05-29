from src.text_utils import escape_xml
from src.poster_theme import TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, BORDER, PANEL_ALT


def render_header(
    data: dict,
    layout: dict
):

    poster = data["poster"]
    box = layout["header"]

    x = box["x"]
    y = box["y"]
    width = box["width"]
    height = box["height"]

    title = escape_xml(
        poster["title"]
    )

    subtitle = escape_xml(
        poster["subtitle"]
    )

    lifecycle = escape_xml(
        poster["lifecycle"]
    )

    domain = escape_xml(
        poster["domain"]
    )

    return [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="28" fill="{PANEL_ALT}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 34}" y="{y + 52}" '
        f'fill="{TEXT_PRIMARY}" font-size="38" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 36}" y="{y + 88}" '
        f'fill="{TEXT_SECONDARY}" font-size="20">'
        f'{subtitle}</text>',

        f'<rect x="{x + width - 520}" y="{y + 34}" width="220" height="44" '
        f'rx="22" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1" />',

        f'<text x="{x + width - 410}" y="{y + 62}" '
        f'fill="#ffffff" font-size="15" text-anchor="middle" font-weight="bold">'
        f'{lifecycle}</text>',

        f'<rect x="{x + width - 280}" y="{y + 34}" width="220" height="44" '
        f'rx="22" fill="#14532d" stroke="#4ade80" stroke-width="1" />',

        f'<text x="{x + width - 170}" y="{y + 62}" '
        f'fill="#ffffff" font-size="15" text-anchor="middle" font-weight="bold">'
        f'{domain}</text>',

        f'<text x="{x + 36}" y="{y + 116}" '
        f'fill="{TEXT_MUTED}" font-size="15">'
        f'Operational Poster Renderer v2 / Level 1 Visibility Board</text>'
    ]
