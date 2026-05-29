from src.text_utils import (
    escape_xml
)
SECTION_COLORS = {
    "source": "#1e293b",
    "telemetry": "#0f766e",
    "analysis": "#5b21b6",
    "recovery": "#b45309",
    "resilience": "#166534",
    "governance": "#334155",
    "validation": "#365314"
}


def render_section(
    section: dict,
    x: int,
    y: int,
    width: int,
    height: int
):

    color = SECTION_COLORS.get(
        section["type"],
        "#1e293b"
    )

    return [
        f'<rect x="{x}" y="{y}" '
        f'width="{width}" height="{height}" '
        f'rx="22" fill="{color}" opacity="0.25" '
        f'stroke="{color}" stroke-width="2" />',

        f'<text x="{x + 20}" y="{y + 34}" '
        f'fill="#ffffff" font-size="22" font-weight="bold">'
        f'{escape_xml(section["label"])}'
        f'</text>'
    ]

