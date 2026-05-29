LANE_COLORS = {
    "Detection": "#0f766e",
    "Correlation": "#5b21b6",
    "Decision": "#7c2d12",
    "Recovery": "#b45309",
    "Validation": "#166534",
    "Governance": "#334155",
    "Failure Domain": "#7f1d1d",
    "Coordination": "#1d4ed8",
    "Failover": "#b91c1c",
    "Survivability": "#15803d",
    "Enterprise Impact": "#7c3aed",
    "Continuity Control": "#0369a1"
}


def render_workflow_lane(
    lane: str,
    y: int,
    width: int
):

    color = LANE_COLORS.get(
        lane,
        "#334155"
    )

    return [
        f'<rect x="40" y="{y}" '
        f'width="{width}" height="80" '
        f'fill="{color}" opacity="0.15" rx="18" />',

        f'<text x="70" y="{y + 48}" '
        f'fill="#ffffff" font-size="24" font-weight="bold">'
        f'{lane}'
        f'</text>'
    ]
