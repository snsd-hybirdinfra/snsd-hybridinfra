from src.poster_theme import BACKGROUND
from src.poster_layout import build_layout
from src.poster_header import render_header
from src.poster_section import render_section, render_section_flow_connector, render_section_flow_connector, render_section_flow_connector
from src.poster_workflow import render_workflow
from src.poster_dashboard import render_dashboards
from src.poster_legend import render_legend
from src.poster_summary import render_summary_panel


def build_poster_svg(
    data: dict
):

    layout = build_layout(
        data
    )

    canvas = layout["canvas"]

    width = canvas["width"]
    height = canvas["height"]

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" fill="{BACKGROUND}" />',
        """
<defs>
<marker id="section-arrow"
markerWidth="12"
markerHeight="12"
refX="10"
refY="6"
orient="auto">
<path d="M0,0 L12,6 L0,12 z" fill="#64748b"/>
</marker>
</defs>
"""
    ]

    elements.extend(
        render_header(
            data,
            layout
        )
    )

    section_layouts = layout["sections"]

    for section in data.get(
        "sections",
        []
    ):

        section_id = section.get(
            "id"
        )

        if section_id not in section_layouts:

            continue

        elements.extend(
            render_section(
                section,
                section_layouts[section_id]
            )
        )

    section_flow = [
        (
            "observed-domain",
            "telemetry-platform",
            "Signals"
        ),
        (
            "telemetry-platform",
            "visibility-output",
            "Visibility"
        ),
        (
            "visibility-output",
            "validation-status",
            "Validate"
        )
    ]

    for source_id, target_id, label in section_flow:

        if source_id in section_layouts and target_id in section_layouts:

            elements.extend(
                render_section_flow_connector(
                    section_layouts[source_id],
                    section_layouts[target_id],
                    label
                )
            )

    elements.extend(
        render_workflow(
            data.get(
                "workflow",
                {}
            ),
            layout
        )
    )

    elements.extend(
        render_dashboards(
            data.get(
                "dashboards",
                []
            ),
            layout
        )
    )

    elements.extend(
        render_summary_panel(
            data,
            layout
        )
    )

    elements.extend(
        render_legend(
            data.get(
                "legend",
                []
            ),
            layout
        )
    )

    elements.append(
        "</svg>"
    )

    return "\n".join(
        elements
    )







