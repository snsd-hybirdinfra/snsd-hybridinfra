ICON_REGISTRY = {
    "network": "🌐",
    "gateway": "🛜",
    "telemetry": "📡",
    "analysis": "🧠",
    "dashboard": "📊",
    "validation": "✅",
    "orchestration": "⚙️",
    "recovery": "🔁",
    "governance": "🛡️",
    "cluster": "☸️",
    "service": "🖥️"
}


def resolve_icon(
    node_type: str
):

    return ICON_REGISTRY.get(
        node_type,
        "⬜"
    )
