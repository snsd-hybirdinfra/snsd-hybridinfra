ANNOTATION_COLORS = {
    "operational": "#38bdf8",
    "validation": "#22c55e",
    "governance": "#94a3b8",
    "incident": "#ef4444"
}


def render_annotation(
    annotation: dict,
    target_position: dict,
    index: int
):

    color = ANNOTATION_COLORS.get(
        annotation.get(
            "annotation_type",
            "operational"
        ),
        "#cbd5e1"
    )

    x = target_position["x"] + 260
    y = target_position["y"] + (index * 72)

    return [
        f'<line x1="{target_position["x"] + 240}" '
        f'y1="{target_position["y"] + 45}" '
        f'x2="{x}" y2="{y}" '
        f'stroke="{color}" stroke-width="2" />',

        f'<rect x="{x}" y="{y - 24}" '
        f'width="320" height="56" '
        f'rx="14" fill="#111827" '
        f'stroke="{color}" />',

        f'<text x="{x + 16}" y="{y + 8}" '
        f'fill="#ffffff" font-size="13">'
        f'{annotation["text"]}'
        f'</text>'
    ]
