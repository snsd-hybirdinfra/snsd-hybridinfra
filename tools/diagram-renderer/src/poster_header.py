from src.text_utils import escape_truncated, escape_xml
from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED


def render_header(
    data: dict,
    layout: dict
):

    poster = data.get(
        "poster",
        data
    )

    header_layout = layout.get(
        "header",
        layout
    )

    x = header_layout["x"]
    y = header_layout["y"]
    width = header_layout["width"]
    height = header_layout["height"]

    title = escape_truncated(
        poster.get("title", ""),
        34
    )

    subtitle = escape_truncated(
        poster.get("subtitle", ""),
        72
    )

    lifecycle = escape_truncated(
        poster.get(
            "lifecycle",
            ""
        ),
        28
    )

    domain = escape_truncated(
        poster.get(
            "domain",
            ""
        ),
        30
    )

    return [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="30" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 38}" y="{y + 52}" '
        f'fill="{TEXT_PRIMARY}" font-size="34" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 40}" y="{y + 88}" '
        f'fill="{TEXT_SECONDARY}" font-size="17">'
        f'{subtitle}</text>',

        f'<rect x="{x + width - 640}" y="{y + 32}" '
        f'width="270" height="38" rx="19" '
        f'fill="#020617" stroke="#334155" stroke-width="1" />',

        f'<text x="{x + width - 505}" y="{y + 57}" '
        f'fill="{TEXT_MUTED}" font-size="13" text-anchor="middle" font-weight="bold">'
        f'{lifecycle}</text>',

        f'<rect x="{x + width - 340}" y="{y + 32}" '
        f'width="280" height="38" rx="19" '
        f'fill="#020617" stroke="#334155" stroke-width="1" />',

        f'<text x="{x + width - 200}" y="{y + 57}" '
        f'fill="{TEXT_MUTED}" font-size="13" text-anchor="middle" font-weight="bold">'
        f'{domain}</text>'
    ]







