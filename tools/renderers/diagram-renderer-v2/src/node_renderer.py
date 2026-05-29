from src.text_utils import (
    escape_xml
)
from src.icon_registry import (
    resolve_icon
)


NODE_COLORS = {
    "connectivity": "#0f766e",
    "observability": "#0369a1",
    "analysis": "#5b21b6",
    "recovery": "#b45309",
    "resilience": "#15803d",
    "governance": "#334155",
    "validation": "#365314",
    "service": "#1d4ed8",
    "platform": "#7c3aed"
}


def render_node(
    node: dict,
    position: dict
):

    x = position["x"]
    y = position["y"]

    icon = resolve_icon(
        node["type"]
    )

    color = NODE_COLORS.get(
        node.get(
            "group",
            "service"
        ),
        "#1e293b"
    )

    elements = []

    elements.append(
        f'<rect x="{x}" y="{y}" '
        f'width="240" height="90" '
        f'rx="16" fill="{color}" '
        f'opacity="0.35" '
        f'stroke="#cbd5e1" />'
    )

    elements.append(
        f'<text x="{x + 20}" y="{y + 38}" '
        f'fill="#ffffff" font-size="22">'
        f'{icon}'
        f'</text>'
    )

    elements.append(
        f'<text x="{x + 60}" y="{y + 38}" '
        f'fill="#ffffff" font-size="18">'
        f'{escape_xml(node["label"])}'
        f'</text>'
    )

    elements.append(
        f'<text x="{x + 60}" y="{y + 64}" '
        f'fill="#cbd5e1" font-size="12">'
        f'{escape_xml(node["type"])}'
        f'</text>'
    )

    return elements

