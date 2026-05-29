from src.text_utils import (
    escape_xml
)
EDGE_COLORS = {
    "telemetry-flow": "#38bdf8",
    "dependency": "#a78bfa",
    "orchestration": "#f59e0b",
    "validation": "#22c55e",
    "failover": "#ef4444",
    "governance-reporting": "#94a3b8"
}


def render_edge(
    edge: dict,
    positions: dict
):

    source = positions[
        edge["from"]
    ]

    target = positions[
        edge["to"]
    ]

    color = EDGE_COLORS.get(
        edge["type"],
        "#94a3b8"
    )

    x1 = source["x"] + 240
    y1 = source["y"] + 45

    x2 = target["x"]
    y2 = target["y"] + 45

    mid_x = (
        x1 + x2
    ) / 2

    mid_y = (
        y1 + y2
    ) / 2 - 12

    return [
        f'<line x1="{x1}" y1="{y1}" '
        f'x2="{x2}" y2="{y2}" '
        f'stroke="{color}" stroke-width="3" />',

        f'<text x="{mid_x}" y="{mid_y}" '
        f'fill="#cbd5e1" font-size="12" '
        f'text-anchor="middle">'
        f'{escape_xml(edge["label"])}'
        f'</text>'
    ]

