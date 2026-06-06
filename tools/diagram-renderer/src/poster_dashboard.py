from src.text_utils import escape_truncated
from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, status_color


def lifecycle_value(data: dict):
    return data.get("poster", {}).get("lifecycle", "")


def dashboard_accent(data: dict):
    lifecycle = lifecycle_value(data)

    if lifecycle == "level-1-visibility":
        return "#2563eb"
    if lifecycle == "level-2-correlation":
        return "#7c3aed"
    if lifecycle == "level-3-recovery":
        return "#0891b2"
    if lifecycle == "level-4-resilience":
        return "#16a34a"
    if lifecycle == "level-5-governance":
        return "#a78bfa"

    return "#38bdf8"


def dashboard_accent_fill(data: dict):
    lifecycle = lifecycle_value(data)

    if lifecycle == "level-1-visibility":
        return "#0b1f4d"
    if lifecycle == "level-2-correlation":
        return "#2e1065"
    if lifecycle == "level-3-recovery":
        return "#164e63"
    if lifecycle == "level-4-resilience":
        return "#052e16"
    if lifecycle == "level-5-governance":
        return "#2e1065"

    return "#082f49"


def dashboard_title_fallback(data: dict):
    lifecycle = lifecycle_value(data)

    if lifecycle == "level-1-visibility":
        return "Visibility Dashboard"
    if lifecycle == "level-2-correlation":
        return "Correlation Dashboard"
    if lifecycle == "level-3-recovery":
        return "Recovery Dashboard"
    if lifecycle == "level-4-resilience":
        return "Resilience Dashboard"
    if lifecycle == "level-5-governance":
        return "Governance Dashboard"

    return "Operational Dashboard"


def dashboard_primary_state(data: dict):
    lifecycle = lifecycle_value(data)

    if lifecycle == "level-1-visibility":
        return ("Visibility State", "VISIBLE", "Telemetry and checks available")
    if lifecycle == "level-2-correlation":
        return ("Impact State", "CORRELATED", "Signals mapped to service impact")
    if lifecycle == "level-3-recovery":
        return ("Recovery State", "READY", "Policy checked and action available")
    if lifecycle == "level-4-resilience":
        return ("Resilience State", "FAILOVER READY", "Continuity path available")
    if lifecycle == "level-5-governance":
        return ("Governance State", "DECISION READY", "Approval and evidence prepared")

    return ("Operational State", "NORMAL", "Operational state available")


def dashboard_result_title(data: dict):
    result = data.get("result", {})

    custom_title = result.get("title", "")

    if custom_title:
        return custom_title

    lifecycle = lifecycle_value(data)

    if lifecycle == "level-1-visibility":
        return "Visibility Result"
    if lifecycle == "level-2-correlation":
        return "Correlation Result"
    if lifecycle == "level-3-recovery":
        return "Recovery Result"
    if lifecycle == "level-4-resilience":
        return "Survivability Result"
    if lifecycle == "level-5-governance":
        return "Governance Result"

    return "Operational Result"


def dashboard_result_body(data: dict):
    result = data.get("result", {})

    custom_description = result.get("description", "")

    if custom_description:
        return custom_description

    lifecycle = lifecycle_value(data)

    if lifecycle == "level-1-visibility":
        return "Visibility signals are collected and validation state is available."
    if lifecycle == "level-2-correlation":
        return "Signals are correlated with service impact and operational context."
    if lifecycle == "level-3-recovery":
        return "Recovery readiness, automation state, and evidence are available."
    if lifecycle == "level-4-resilience":
        return "Failover readiness and survivability state are available."
    if lifecycle == "level-5-governance":
        return "Decision, approval, and governance evidence are available."

    return "Operational state is available."


def normalize_dashboard(data: dict):
    dashboards = data.get("dashboards", [])

    if isinstance(dashboards, dict):
        return dashboards

    if isinstance(dashboards, list):
        for dashboard in dashboards:
            if isinstance(dashboard, dict):
                return dashboard

    return {}


def normalize_widgets(dashboard: dict):
    widgets = dashboard.get("widgets", [])

    if isinstance(widgets, dict):
        widgets = [widgets]

    if not isinstance(widgets, list):
        return []

    normalized = []

    for widget in widgets:
        if isinstance(widget, dict):
            normalized.append(widget)

    return normalized[:6]


def render_dashboards(data: dict, layout: dict):
    dashboard_layout = layout.get("dashboard", layout)

    x = dashboard_layout["x"]
    y = dashboard_layout["y"]
    width = dashboard_layout["width"]
    height = dashboard_layout["height"]

    dashboard = normalize_dashboard(data)
    widgets = normalize_widgets(dashboard)

    accent = dashboard_accent(data)
    accent_fill = dashboard_accent_fill(data)

    state_label, state_value, state_detail = dashboard_primary_state(data)

    title = escape_truncated(
        dashboard.get("title", dashboard_title_fallback(data)),
        42
    )

    subtitle = escape_truncated(
        dashboard.get("subtitle", "Operational status and validation metrics"),
        82
    )

    state_label = escape_truncated(state_label, 24)
    state_value = escape_truncated(state_value, 26)
    state_detail = escape_truncated(state_detail, 46)

    result_title = escape_truncated(dashboard_result_title(data), 30)
    result_body = escape_truncated(dashboard_result_body(data), 76)

    content_y = y + 118
    card_height = 215 if height >= 400 else 150
    signal_y = y + height - 66

    elements = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="30" fill="{PANEL}" stroke="{BORDER}" stroke-width="2" />',

        f'<rect x="{x + 24}" y="{y + 22}" width="{width - 48}" height="70" '
        f'rx="22" fill="#020617" stroke="{accent}" stroke-width="2" opacity="0.96" />',

        f'<text x="{x + 48}" y="{y + 52}" '
        f'fill="{TEXT_PRIMARY}" font-size="24" font-weight="bold">{title}</text>',

        f'<text x="{x + 48}" y="{y + 78}" '
        f'fill="{TEXT_SECONDARY}" font-size="13">{subtitle}</text>',

        f'<rect x="{x + 34}" y="{content_y}" width="430" height="{card_height}" '
        f'rx="26" fill="{accent_fill}" stroke="{accent}" stroke-width="4" opacity="0.98" />',

        f'<text x="{x + 62}" y="{content_y + 42}" '
        f'fill="{TEXT_MUTED}" font-size="13" font-weight="bold">{state_label}</text>',

        f'<text x="{x + 62}" y="{content_y + 92}" '
        f'fill="{TEXT_PRIMARY}" font-size="30" font-weight="bold">{state_value}</text>',

        f'<rect x="{x + 62}" y="{content_y + 120}" width="320" height="32" '
        f'rx="16" fill="#020617" stroke="{accent}" stroke-width="1" />',

        f'<text x="{x + 78}" y="{content_y + 141}" '
        f'fill="{TEXT_SECONDARY}" font-size="12" font-weight="bold">{state_detail}</text>'
    ]

    widget_start_x = x + 500
    widget_start_y = content_y
    widget_width = 205
    widget_height = 92 if height >= 400 else 68
    widget_gap = 22
    row_gap = 30 if height >= 400 else 20

    for index, widget in enumerate(widgets[:6]):
        col = index % 3
        row = index // 3

        wx = widget_start_x + col * (widget_width + widget_gap)
        wy = widget_start_y + row * (widget_height + row_gap)

        label = escape_truncated(widget.get("label", ""), 22)
        value = escape_truncated(widget.get("value", ""), 20)
        status = widget.get("status", "")

        color = status_color(status)

        elements.extend(
            [
                f'<rect x="{wx}" y="{wy}" width="{widget_width}" height="{widget_height}" '
                f'rx="20" fill="#0f172a" stroke="{color}" stroke-width="2" opacity="0.98" />',

                f'<rect x="{wx + 14}" y="{wy + 12}" width="10" height="{widget_height - 24}" '
                f'rx="5" fill="{color}" opacity="0.85" />',

                f'<text x="{wx + 40}" y="{wy + 30}" '
                f'fill="{TEXT_MUTED}" font-size="11" font-weight="bold">{label}</text>',

                f'<text x="{wx + 40}" y="{wy + 58}" '
                f'fill="{TEXT_PRIMARY}" font-size="16" font-weight="bold">{value}</text>'
            ]
        )

    result_x = x + width - 500

    elements.extend(
        [
            f'<rect x="{result_x}" y="{content_y}" width="455" height="{card_height}" '
            f'rx="26" fill="#020617" stroke="{accent}" stroke-width="3" opacity="0.98" />',

            f'<text x="{result_x + 28}" y="{content_y + 42}" '
            f'fill="{TEXT_PRIMARY}" font-size="19" font-weight="bold">{result_title}</text>',

            f'<rect x="{result_x + 28}" y="{content_y + 64}" width="220" height="30" '
            f'rx="15" fill="#0f172a" stroke="{accent}" stroke-width="1" />',

            f'<text x="{result_x + 138}" y="{content_y + 84}" '
            f'fill="{TEXT_SECONDARY}" font-size="11" text-anchor="middle" font-weight="bold">'
            f'DASHBOARD RESULT</text>',

            f'<text x="{result_x + 28}" y="{content_y + 124}" '
            f'fill="{TEXT_MUTED}" font-size="13">{result_body}</text>'
        ]
    )

    return elements









