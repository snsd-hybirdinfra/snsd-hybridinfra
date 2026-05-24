from pathlib import Path
from typing import Optional

from src.dependency_loader import (
    load_dependencies
)


STATUS_COLORS = {
    "COMPLETED": "#16a34a",
    "WARNING": "#facc15",
    "FAILED": "#dc2626",
    "BLOCKED": "#64748b",
    "SKIPPED": "#94a3b8",
    "UNKNOWN": "#334155"
}


EDGE_STATUS_COLORS = {
    "COMPLETED": "#22c55e",
    "WARNING": "#facc15",
    "FAILED": "#dc2626",
    "BLOCKED": "#64748b",
    "SKIPPED": "#94a3b8",
    "UNKNOWN": "#94a3b8"
}


def build_result_map(
    execution_results: Optional[list]
):

    result_map = {}

    if not execution_results:

        return result_map

    for result in execution_results:

        result_map[
            result.get("tool")
        ] = result

    return result_map


def get_status(
    tool: str,
    result_map: dict
):

    return result_map.get(
        tool,
        {}
    ).get(
        "status",
        "UNKNOWN"
    )


def get_duration(
    tool: str,
    result_map: dict
):

    return result_map.get(
        tool,
        {}
    ).get(
        "duration_seconds",
        ""
    )


def get_node_color(
    status: str,
    duration
):

    if status in [
        "FAILED",
        "BLOCKED",
        "WARNING"
    ]:

        return STATUS_COLORS.get(
            status,
            STATUS_COLORS["UNKNOWN"]
        )

    try:

        duration_value = float(
            duration
        )

    except (
        TypeError,
        ValueError
    ):

        return STATUS_COLORS.get(
            status,
            STATUS_COLORS["UNKNOWN"]
        )

    if duration_value >= 30:

        return "#ea580c"

    if duration_value >= 10:

        return "#f97316"

    return STATUS_COLORS.get(
        status,
        STATUS_COLORS["UNKNOWN"]
    )


def build_layers(
    dependencies: dict
):

    layer_map = {}

    def resolve_layer(tool: str):

        if tool in layer_map:

            return layer_map[tool]

        depends_on = dependencies.get(
            tool,
            {}
        ).get(
            "depends_on",
            []
        )

        if not depends_on:

            layer_map[tool] = 0

            return 0

        layer = (
            max(
                resolve_layer(dependency)
                for dependency in depends_on
            )
            + 1
        )

        layer_map[tool] = layer

        return layer

    all_tools = set(dependencies.keys())

    for config in dependencies.values():

        for dependency in config.get("depends_on", []):

            all_tools.add(dependency)

    for tool in all_tools:

        resolve_layer(tool)

    layers = {}

    for tool, layer in layer_map.items():

        layers.setdefault(
            layer,
            []
        ).append(tool)

    for layer_tools in layers.values():

        layer_tools.sort()

    return layers


def build_positions(
    layers: dict
):

    positions = {}

    start_x = 80
    start_y = 150
    gap_x = 300
    gap_y = 112

    for layer, tools in sorted(layers.items()):

        for index, tool in enumerate(tools):

            positions[tool] = {
                "x": start_x + layer * gap_x,
                "y": start_y + index * gap_y
            }

    return positions


def get_edge_color(
    source_tool: str,
    result_map: dict
):

    source_status = get_status(
        source_tool,
        result_map
    )

    return EDGE_STATUS_COLORS.get(
        source_status,
        EDGE_STATUS_COLORS["UNKNOWN"]
    )


def render_legend(
    lines: list
):

    legend_items = [
        ("COMPLETED", "#16a34a"),
        ("WARNING", "#facc15"),
        ("FAILED", "#dc2626"),
        ("BLOCKED", "#64748b"),
        ("SLOW >=10s", "#f97316"),
        ("VERY SLOW >=30s", "#ea580c")
    ]

    x = 40
    y = 105

    for label, color in legend_items:

        lines.append(
            f'<rect x="{x}" y="{y}" width="14" height="14" '
            f'rx="3" fill="{color}" />'
        )

        lines.append(
            f'<text x="{x + 22}" y="{y + 12}" '
            f'fill="#cbd5e1" font-size="12">'
            f'{label}'
            f'</text>'
        )

        x += 145


def render_execution_graph(
    run_context: dict,
    execution_results: Optional[list] = None
):

    run_path = Path(
        run_context["workspace"]
    )

    svg_path = (
        run_path
        / "execution-graph.svg"
    )

    dependencies = load_dependencies()

    result_map = build_result_map(
        execution_results
    )

    layers = build_layers(
        dependencies
    )

    positions = build_positions(
        layers
    )

    max_x = max(
        position["x"]
        for position in positions.values()
    )

    max_y = max(
        position["y"]
        for position in positions.values()
    )

    width = max(
        1500,
        max_x + 390
    )

    height = max(
        720,
        max_y + 180
    )

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#0f172a" />',
        '<defs>',
        '<marker id="arrow" markerWidth="10" markerHeight="10" '
        'refX="9" refY="3" orient="auto" markerUnits="strokeWidth">',
        '<path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />',
        '</marker>',
        '</defs>',
        '<text x="40" y="50" fill="#ffffff" font-size="26" font-weight="bold">',
        'Tool Execution DAG',
        '</text>',
        '<text x="40" y="82" fill="#cbd5e1" font-size="14">',
        f'Run ID: {run_context.get("run_id", "unknown")}',
        '</text>'
    ]

    render_legend(
        lines
    )

    for tool, config in dependencies.items():

        target = positions.get(tool)

        if not target:

            continue

        for dependency in config.get("depends_on", []):

            source = positions.get(dependency)

            if not source:

                continue

            edge_color = get_edge_color(
                dependency,
                result_map
            )

            lines.append(
                f'<line '
                f'x1="{source["x"] + 250}" '
                f'y1="{source["y"] + 36}" '
                f'x2="{target["x"]}" '
                f'y2="{target["y"] + 36}" '
                f'stroke="{edge_color}" '
                f'stroke-width="2.5" '
                f'marker-end="url(#arrow)" />'
            )

    for tool, pos in positions.items():

        status = get_status(
            tool,
            result_map
        )

        duration = get_duration(
            tool,
            result_map
        )

        color = get_node_color(
            status,
            duration
        )

        critical = dependencies.get(
            tool,
            {}
        ).get(
            "critical",
            True
        )

        policy_label = (
            "critical"
            if critical
            else "non-critical"
        )

        duration_label = (
            f"{duration}s"
            if duration != ""
            else "n/a"
        )

        lines.append(
            f'<rect x="{pos["x"]}" y="{pos["y"]}" '
            f'width="250" height="74" rx="12" '
            f'fill="{color}" stroke="#e2e8f0" stroke-width="1.5" />'
        )

        lines.append(
            f'<text x="{pos["x"] + 14}" y="{pos["y"] + 24}" '
            f'fill="#ffffff" font-size="13" font-weight="bold">'
            f'{tool}'
            f'</text>'
        )

        lines.append(
            f'<text x="{pos["x"] + 14}" y="{pos["y"] + 47}" '
            f'fill="#f8fafc" font-size="11">'
            f'{status} / {policy_label}'
            f'</text>'
        )

        lines.append(
            f'<text x="{pos["x"] + 14}" y="{pos["y"] + 64}" '
            f'fill="#f8fafc" font-size="10">'
            f'duration: {duration_label}'
            f'</text>'
        )

    lines.append(
        "</svg>"
    )

    svg_path.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    return {
        "svg": svg_path
    }
