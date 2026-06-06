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

    "signal-domain": "#2563eb",
    "correlation-platform": "#7c3aed",
    "impact-analysis": "#dc2626",
    "operational-insight": "#16a34a",

    "incident-trigger": "#dc2626",
    "recovery-control": "#7c3aed",
    "automation-execution": "#0891b2",
    "recovery-validation": "#16a34a",

    "failure-domain": "#dc2626",
    "resilience-coordination": "#7c3aed",
    "failover-execution": "#0891b2",
    "survivability-validation": "#16a34a",

    "continuity-scope": "#2563eb",
    "governance-control": "#7c3aed",
    "executive-coordination": "#0891b2",
    "evidence-reporting": "#16a34a",

    "default": "#475569",
}

STATUS_COLORS = {
    "observed": "#60a5fa",
    "monitored": "#38bdf8",
    "reachable": "#93c5fd",
    "collecting": "#22d3ee",
    "collected": "#38bdf8",
    "streaming": "#06b6d4",
    "active": "#14b8a6",
    "visible": "#22c55e",

    "detected": "#fb923c",
    "triggered": "#ef4444",
    "impacted": "#ef4444",
    "qualified": "#f97316",
    "warning": "#fb923c",
    "degraded": "#fb923c",

    "analyzing": "#a78bfa",
    "correlated": "#8b5cf6",
    "assessed": "#f97316",
    "calculated": "#facc15",
    "mapped": "#818cf8",
    "reviewed": "#a78bfa",
    "evaluating": "#a78bfa",

    "ready": "#84cc16",
    "prepared": "#22c55e",
    "selected": "#38bdf8",
    "scoped": "#60a5fa",
    "decided": "#facc15",
    "approved": "#22c55e",
    "checked": "#facc15",
    "verified": "#facc15",

    "executed": "#06b6d4",
    "running": "#06b6d4",
    "tracked": "#38bdf8",
    "recorded": "#94a3b8",

    "validated": "#84cc16",
    "passed": "#22c55e",
    "stable": "#22c55e",
    "healthy": "#22c55e",
    "normal": "#10b981",
    "available": "#4ade80",
    "published": "#22c55e",
    "reported": "#22c55e",
    "generated": "#94a3b8",
    "reviewable": "#94a3b8",

    "default": "#94a3b8",
}


def section_color(section_id: str):
    return SECTION_COLORS.get(
        section_id,
        SECTION_COLORS["default"],
    )


def status_color(status: str):
    normalized = str(status or "").strip().lower()

    return STATUS_COLORS.get(
        normalized,
        STATUS_COLORS["default"],
    )


