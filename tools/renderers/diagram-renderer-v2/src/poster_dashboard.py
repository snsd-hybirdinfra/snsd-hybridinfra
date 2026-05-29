from src.text_utils import escape_xml
from src.poster_theme import PANEL_ALT, PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED


WIDGET_COLORS = {
    "healthy": "#22c55e",
    "normal": "#38bdf8",
    "verified": "#facc15",
    "warning": "#fb923c",
    "critical": "#ef4444",
    "default": "#94a3b8"
}


def widget_color(
    status: str
):

    return WIDGET_COLORS.get(
        status,
        WIDGET_COLORS["default"]
    )


def render_dashboards(
    dashboards: list,
    layout: dict
):

    box = layout["dashboard"]

    x = box["x"]
    y = box["y"]
    width = box["width"]
    height = box["height"]

    widgets = []

    for dashboard in dashboards:

        for widget in dashboard.get(
            "widgets",
            []
        ):

            widgets.append(
                widget
            )

    overall = widgets[0] if widgets else {
        "label": "Overall Health",
        "value": "Healthy",
        "status": "healthy"
    }

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="30" fill="{PANEL_ALT}" stroke="{BORDER}" stroke-width="2" />',

        f'<text x="{x + 34}" y="{y + 44}" '
        f'fill="{TEXT_PRIMARY}" font-size="26" font-weight="bold">'
        f'Operational Status Dashboard</text>',

        f'<text x="{x + 34}" y="{y + 74}" '
        f'fill="{TEXT_MUTED}" font-size="15">'
        f'Visibility health, signal continuity, and validation status</text>'
    ]

    elements.extend(
        render_health_score_card(
            overall,
            x + 34,
            y + 96,
            390,
            112
        )
    )

    kpi_x = x + 455
    kpi_y = y + 96

    for index, widget in enumerate(
        widgets[1:5]
    ):

        current_x = kpi_x + index * 318

        elements.extend(
            render_kpi_card(
                widget,
                current_x,
                kpi_y,
                290,
                112
            )
        )

    elements.extend(
        render_validation_statement(
            x + 455,
            y + 224,
            width - 505,
            58
        )
    )

    return elements


def render_health_score_card(
    widget: dict,
    x: int,
    y: int,
    width: int,
    height: int
):

    label = escape_xml(
        "Overall Visibility Health"
    )

    value = escape_xml(
        widget.get(
            "value",
            "Healthy"
        )
    )

    color = widget_color(
        widget.get(
            "status",
            "healthy"
        )
    )

    return [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="26" fill="{PANEL}" stroke="{color}" stroke-width="3" />',

        f'<text x="{x + 24}" y="{y + 36}" '
        f'fill="{TEXT_SECONDARY}" font-size="15">'
        f'{label}</text>',

        f'<text x="{x + 24}" y="{y + 82}" '
        f'fill="{TEXT_PRIMARY}" font-size="34" font-weight="bold">'
        f'{value}</text>',

        f'<circle cx="{x + width - 54}" cy="{y + 62}" r="34" '
        f'fill="#020617" stroke="{color}" stroke-width="5" />',

        f'<text x="{x + width - 54}" y="{y + 73}" '
        f'fill="{color}" font-size="28" text-anchor="middle" font-weight="bold">'
        f'✓</text>'
    ]


def render_kpi_card(
    widget: dict,
    x: int,
    y: int,
    width: int,
    height: int
):

    label = escape_xml(
        widget.get(
            "label",
            ""
        )
    )

    value = escape_xml(
        widget.get(
            "value",
            ""
        )
    )

    color = widget_color(
        widget.get(
            "status",
            "default"
        )
    )

    return [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="22" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<circle cx="{x + width - 30}" cy="{y + 30}" r="9" '
        f'fill="{color}" />',

        f'<text x="{x + 22}" y="{y + 38}" '
        f'fill="{TEXT_SECONDARY}" font-size="14">'
        f'{label}</text>',

        f'<text x="{x + 22}" y="{y + 82}" '
        f'fill="{TEXT_PRIMARY}" font-size="26" font-weight="bold">'
        f'{value}</text>',

        f'<rect x="{x + 22}" y="{y + height - 22}" '
        f'width="{width - 44}" height="6" rx="3" '
        f'fill="#020617" />',

        f'<rect x="{x + 22}" y="{y + height - 22}" '
        f'width="{int((width - 44) * 0.82)}" height="6" rx="3" '
        f'fill="{color}" />'
    ]



def render_signal_matrix(
    widgets: list,
    x: int,
    y: int,
    width: int,
    height: int
):

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="18" fill="#020617" stroke="{BORDER}" stroke-width="1" />',

        f'<text x="{x + 20}" y="{y + 36}" '
        f'fill="{TEXT_MUTED}" font-size="13" font-weight="bold">'
        f'Visibility Signal Matrix</text>'
    ]

    matrix_x = x + 220
    matrix_y = y + 11

    cell_width = 180
    cell_height = 22
    cell_gap = 24

    for index, widget in enumerate(
        widgets[:4]
    ):

        color = widget_color(
            widget.get(
                "status",
                "default"
            )
        )

        label = escape_xml(
            widget.get(
                "label",
                ""
            )
        )

        current_x = matrix_x + index * (
            cell_width + cell_gap
        )

        if current_x + cell_width > x + width - 20:

            break

        elements.extend(
            [
                f'<rect x="{current_x}" y="{matrix_y}" '
                f'width="{cell_width}" height="{cell_height}" rx="11" '
                f'fill="{color}" opacity="0.85" />',

                f'<text x="{current_x + cell_width / 2}" y="{matrix_y + 15}" '
                f'fill="#020617" font-size="10" text-anchor="middle" font-weight="bold">'
                f'{label}</text>'
            ]
        )

    return elements





def render_validation_statement(
    x: int,
    y: int,
    width: int,
    height: int
):

    return [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="18" fill="#020617" stroke="#334155" stroke-width="1" />',

        f'<text x="{x + 20}" y="{y + 36}" '
        f'fill="#22c55e" font-size="13" font-weight="bold">'
        f'Validation Result</text>',

        f'<text x="{x + 178}" y="{y + 36}" '
        f'fill="#cbd5e1" font-size="13">'
        f'All monitored VPN connectivity signals are visible, streaming, and operationally validated.</text>'
    ]





