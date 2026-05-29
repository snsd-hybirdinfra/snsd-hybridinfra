LEGEND_ITEMS = [
    ("🌐", "Connectivity"),
    ("📡", "Observability"),
    ("🧠", "Analysis"),
    ("⚙️", "Recovery"),
    ("🛡️", "Governance"),
    ("✅", "Validation")
]


def render_legend(
    x: int,
    y: int
):

    elements = [
        f'<rect x="{x}" y="{y}" width="300" height="240" '
        f'rx="20" fill="#111827" stroke="#64748b" />',

        f'<text x="{x + 20}" y="{y + 36}" '
        f'fill="#ffffff" font-size="20" font-weight="bold">'
        f'Legend'
        f'</text>'
    ]

    offset_y = y + 72

    for icon, label in LEGEND_ITEMS:

        elements.append(
            f'<text x="{x + 24}" y="{offset_y}" '
            f'fill="#ffffff" font-size="18">'
            f'{icon}'
            f'</text>'
        )

        elements.append(
            f'<text x="{x + 64}" y="{offset_y}" '
            f'fill="#cbd5e1" font-size="14">'
            f'{label}'
            f'</text>'
        )

        offset_y += 28

    return elements
