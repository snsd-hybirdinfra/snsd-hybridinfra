from src.section_renderer import (
    render_section
)

from src.edge_renderer import (
    render_edge
)

from src.workflow_lane_renderer import (
    render_workflow_lane
)

from src.layout_engine import (
    build_layout
)

from src.section_layout_engine import (
    build_section_layout
)

from src.node_renderer import (
    render_node
)

from src.dashboard_renderer import (
    render_dashboard
)

from src.legend_renderer import (
    render_legend
)

from src.annotation_renderer import (
    render_annotation
)


def build_svg(
    data: dict,
    profile: dict
):

    width = 1900
    height = 1000

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#0f172a" />'
    ]

    if profile.get(
        "lane_enabled"
    ):

        lane_y = 20

        for lane in data.get(
            "workflow_lanes",
            []
        ):

            svg.extend(
                render_workflow_lane(
                    lane,
                    lane_y,
                    width - 80
                )
            )

            lane_y += 110

    section_layouts = build_section_layout(
        data,
        profile
    )

    for section in data["sections"]:

        layout = section_layouts[
            section["id"]
        ]

        svg.extend(
            render_section(
                section,
                layout["x"],
                layout["y"],
                layout["width"],
                layout["height"]
            )
        )

    positions = build_layout(
        data,
        profile
    )

    for edge in data["edges"]:

        svg.extend(
            render_edge(
                edge,
                positions
            )
        )

    for node in data["nodes"]:

        pos = positions[
            node["id"]
        ]

        x = pos["x"]
        y = pos["y"]

        svg.extend(
            render_node(
                node,
                pos
            )
        )


    dashboard_y = 760

    for dashboard in data.get(
        "dashboards",
        []
    ):

        svg.extend(
            render_dashboard(
                dashboard,
                1460,
                dashboard_y
            )
        )

        dashboard_y += 210

    annotation_index = 0

    for annotation in data.get(
        "annotations",
        []
    ):

        target = positions.get(
            annotation["target"]
        )

        if not target:

            continue

        svg.extend(
            render_annotation(
                annotation,
                target,
                annotation_index
            )
        )

        annotation_index += 1

    svg.extend(
        render_legend(
            40,
            720
        )
    )

    svg.append(
        "</svg>"
    )

    return "\n".join(
        svg
    )







