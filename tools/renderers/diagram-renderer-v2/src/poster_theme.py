BACKGROUND = "#0f172a"
PANEL = "#111827"
PANEL_ALT = "#1e293b"
BORDER = "#334155"

TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#cbd5e1"
TEXT_MUTED = "#94a3b8"

SECTION_COLORS = {
    "observed-domain": "#2563eb",
    "telemetry-platform": "#0891b2",
    "visibility-output": "#16a34a",
    "validation-status": "#ca8a04",
    "default": "#475569"
}

STATUS_COLORS = {
    "Observed": "#60a5fa",
    "Monitored": "#38bdf8",
    "Reachable": "#93c5fd",
    "Collecting": "#22d3ee",
    "Streaming": "#06b6d4",
    "Active": "#14b8a6",
    "Visible": "#22c55e",
    "Ready": "#84cc16",
    "Available": "#4ade80",
    "Healthy": "#22c55e",
    "Normal": "#10b981",
    "Verified": "#facc15",
    "default": "#94a3b8"
}


def section_color(
    section_id: str
):

    return SECTION_COLORS.get(
        section_id,
        SECTION_COLORS["default"]
    )


def status_color(
    status: str
):

    return STATUS_COLORS.get(
        status,
        STATUS_COLORS["default"]
    )
