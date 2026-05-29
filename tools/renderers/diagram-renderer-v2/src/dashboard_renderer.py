def render_dashboard(
    dashboard: dict,
    x: int,
    y: int
):

    elements = [
        f'<rect x="{x}" y="{y}" width="360" height="180" '
        f'rx="20" fill="#111827" stroke="#38bdf8" stroke-width="2" />',

        f'<text x="{x + 20}" y="{y + 36}" '
        f'fill="#ffffff" font-size="20" font-weight="bold">'
        f'{dashboard["title"]}'
        f'</text>'
    ]

    metric_y = y + 70

    for metric in dashboard.get(
        "metrics",
        []
    ):

        for key, value in metric.items():

            elements.append(
                f'<text x="{x + 24}" y="{metric_y}" '
                f'fill="#cbd5e1" font-size="14">'
                f'{key}: {value}'
                f'</text>'
            )

            metric_y += 26

    return elements
