from src.poster_theme import PANEL_ALT, PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED
from src.text_utils import escape_xml


def render_summary_panel(
    data: dict,
    layout: dict
):

    box = layout["summary"]

    x = box["x"]
    y = box["y"]
    width = box["width"]
    height = box["height"]

    sections = data.get(
        "sections",
        []
    )

    total_sections = len(
        sections
    )

    total_cards = sum(
        len(
            section.get(
                "cards",
                []
            )
        )
        for section in sections
    )

    summary_items = [
        {
            "label": "Monitored Domains",
            "value": count_cards(
                data,
                "observed-domain"
            )
        },
        {
            "label": "Signal Sources",
            "value": count_cards(
                data,
                "telemetry-platform"
            )
        },
        {
            "label": "Output Views",
            "value": count_cards(
                data,
                "visibility-output"
            )
        },
        {
            "label": "Validation Checks",
            "value": count_cards(
                data,
                "validation-status"
            )
        }
    ]

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="30" fill="{PANEL_ALT}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 34}" y="{y + 44}" '
        f'fill="{TEXT_PRIMARY}" font-size="24" font-weight="bold">'
        f'Visibility Coverage Summary</text>',

        f'<text x="{x + 34}" y="{y + 72}" '
        f'fill="{TEXT_MUTED}" font-size="14">'
        f'Scenario visibility scope and validation coverage</text>',

        f'<rect x="{x + width - 150}" y="{y + 28}" '
        f'width="104" height="36" rx="18" '
        f'fill="#020617" stroke="#38bdf8" stroke-width="1" />',

        f'<text x="{x + width - 98}" y="{y + 52}" '
        f'fill="#38bdf8" font-size="13" text-anchor="middle" font-weight="bold">'
        f'{total_cards} SIGNALS</text>'
    ]

    start_x = x + 34
    start_y = y + 100

    item_width = 214
    item_height = 68
    item_gap = 16

    for index, item in enumerate(
        summary_items
    ):

        current_x = start_x + (
            index % 2
        ) * (
            item_width + item_gap
        )

        current_y = start_y + (
            index // 2
        ) * (
            item_height + item_gap
        )

        label = escape_xml(
            item["label"]
        )

        value = escape_xml(
            item["value"]
        )

        elements.extend(
            [
                f'<rect x="{current_x}" y="{current_y}" '
                f'width="{item_width}" height="{item_height}" '
                f'rx="20" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

                f'<text x="{current_x + 20}" y="{current_y + 30}" '
                f'fill="{TEXT_SECONDARY}" font-size="13">'
                f'{label}</text>',

                f'<text x="{current_x + 20}" y="{current_y + 58}" '
                f'fill="{TEXT_PRIMARY}" font-size="24" font-weight="bold">'
                f'{value}</text>'
            ]
        )

    return elements


def count_cards(
    data: dict,
    section_id: str
):

    for section in data.get(
        "sections",
        []
    ):

        if section.get(
            "id"
        ) == section_id:

            return len(
                section.get(
                    "cards",
                    []
                )
            )

    return 0

