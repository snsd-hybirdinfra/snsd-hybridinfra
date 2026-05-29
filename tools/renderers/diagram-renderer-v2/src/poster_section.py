from src.text_utils import escape_xml
from src.poster_theme import PANEL_ALT, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, section_color
from src.poster_card import render_card


def render_section(
    section: dict,
    layout: dict
):

    x = layout["x"]
    y = layout["y"]
    width = layout["width"]
    height = layout["height"]

    title = escape_xml(
        section.get(
            "title",
            ""
        )
    )

    description = escape_xml(
        section.get(
            "description",
            ""
        )
    )

    summary = escape_xml(
        section.get(
            "summary",
            ""
        )
    )

    color = section_color(
        section.get(
            "id",
            "default"
        )
    )

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="28" fill="{PANEL_ALT}" stroke="{color}" stroke-width="3" />',

        f'<rect x="{x}" y="{y}" width="14" height="{height}" '
        f'rx="7" fill="{color}" />',

        f'<text x="{x + 34}" y="{y + 42}" '
        f'fill="{TEXT_PRIMARY}" font-size="24" font-weight="bold">'
        f'{title}</text>',

        f'<text x="{x + 34}" y="{y + 70}" '
        f'fill="{TEXT_SECONDARY}" font-size="15">'
        f'{description}</text>'
    ]

    if summary:

        elements.extend(
            [
                f'<rect x="{x + width - 270}" y="{y + 26}" '
                f'width="220" height="38" rx="19" '
                f'fill="#020617" stroke="{color}" stroke-width="2" />',

                f'<text x="{x + width - 160}" y="{y + 51}" '
                f'fill="{color}" font-size="13" text-anchor="middle" font-weight="bold">'
                f'{summary}</text>'
            ]
        )

    cards = section.get(
        "cards",
        []
    )

    card_width = 540
    card_height = 112
    card_gap = 34

    card_x = x + 34
    card_y = y + 92

    for index, card in enumerate(
        cards
    ):

        current_x = card_x + index * (
            card_width + card_gap
        )

        elements.extend(
            render_card(
                card,
                current_x,
                card_y,
                card_width,
                card_height
            )
        )

    return elements



def render_section_flow_connector(
    from_layout: dict,
    to_layout: dict,
    label: str
):

    x = from_layout["x"] + from_layout["width"] / 2

    y1 = from_layout["y"] + from_layout["height"] + 10
    y2 = to_layout["y"] - 28

    arrow_tip_y = to_layout["y"] - 10
    arrow_base_y = to_layout["y"] - 26

    return [
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" '
        f'stroke="#475569" stroke-width="2" stroke-linecap="round" '
        f'stroke-dasharray="8 8" opacity="0.7" />',

        f'<polygon points="{x - 9},{arrow_base_y} {x + 9},{arrow_base_y} {x},{arrow_tip_y}" '
        f'fill="#64748b" opacity="0.85" />'
    ]
