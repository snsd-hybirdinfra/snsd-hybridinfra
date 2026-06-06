from src.poster_layout import build_layout
from src.poster_header import render_header
from src.poster_section import render_section, render_section_flow_connector
from src.poster_workflow import render_workflow
from src.poster_dashboard import render_dashboards
from src.poster_legend import render_legend
from src.poster_summary import render_summary_panel


def build_poster_svg(
    data: dict
):

    poster = data.get(
        "poster",
        {}
    )

    layout = build_layout(
        poster
    )

    canvas = layout.get(
        "canvas",
        {}
    )

    width = canvas.get(
        "width",
        poster.get(
            "width",
            2600
        )
    )

    height = canvas.get(
        "height",
        poster.get(
            "height",
            1900
        )
    )

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Arial, Helvetica, sans-serif">',
        '<style>text { font-family: Arial, Helvetica, sans-serif; letter-spacing: normal; word-spacing: normal; text-rendering: optimizeLegibility; font-kerning: normal; }</style>',
        '<style>text { font-family: Arial, Helvetica, sans-serif; letter-spacing: normal; word-spacing: normal; text-rendering: optimizeLegibility; font-kerning: normal; }</style>',
        f'<rect width="{width}" height="{height}" fill="#020617" />'
    ]

    svg_parts.extend(
        render_header(
            data,
            layout
        )
    )

    section_layouts = layout.get(
        "sections",
        {}
    )

    for section in data.get(
        "sections",
        []
    ):

        section_id = section.get(
            "id"
        )

        if section_id not in section_layouts:

            continue

        svg_parts.extend(
            render_section(
                section,
                section_layouts[section_id]
            )
        )

    for from_id, to_id, label in get_section_flow(
        data
    ):

        if from_id not in section_layouts or to_id not in section_layouts:

            continue

        svg_parts.extend(
            render_section_flow_connector(
                section_layouts[from_id],
                section_layouts[to_id],
                label
            )
        )

    svg_parts.extend(
        render_workflow(
            data,
            layout
        )
    )

    svg_parts.extend(
        render_summary_panel(
            data,
            layout
        )
    )

    svg_parts.extend(
        render_dashboards(
            data,
            layout
        )
    )

    svg_parts.extend(
        render_legend(
            data,
            layout
        )
    )

    svg_parts.append(
        "</svg>"
    )

    return "\n".join(
        svg_parts
    )


def get_section_flow(
    data: dict
):

    lifecycle = data.get(
        "poster",
        {}
    ).get(
        "lifecycle",
        ""
    )

    if lifecycle == "level-1-visibility":

        return [
            ("observed-domain", "telemetry-platform", ""),
            ("telemetry-platform", "visibility-output", ""),
            ("visibility-output", "validation-status", "")
        ]

    if lifecycle == "level-2-correlation":

        return [
            ("signal-domain", "correlation-platform", ""),
            ("correlation-platform", "impact-analysis", ""),
            ("impact-analysis", "operational-insight", "")
        ]

    if lifecycle == "level-3-recovery":

        return [
            ("incident-trigger", "recovery-control", ""),
            ("recovery-control", "automation-execution", ""),
            ("automation-execution", "recovery-validation", "")
        ]

    if lifecycle == "level-4-resilience":

        return [
            ("failure-domain", "resilience-coordination", ""),
            ("resilience-coordination", "failover-execution", ""),
            ("failover-execution", "survivability-validation", "")
        ]

    if lifecycle == "level-5-governance":

        return [
            ("continuity-scope", "governance-control", ""),
            ("governance-control", "executive-coordination", ""),
            ("executive-coordination", "evidence-reporting", "")
        ]

    return []






