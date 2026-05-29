def build_layout(
    data: dict,
    profile: dict
):

    direction = profile[
        "direction"
    ]

    if direction == "fan-in":

        return build_fan_in_layout(
            data
        )

    if direction == "distributed":

        return build_distributed_layout(
            data
        )

    return build_linear_layout(
        data
    )


def build_linear_layout(
    data: dict
):

    positions = {}

    section_positions = {}

    section_x = 100

    for section in data["sections"]:

        section_positions[
            section["id"]
        ] = section_x

        section_x += 340

    section_offsets = {}

    for node in data["nodes"]:

        section_id = node["section"]

        x = section_positions[
            section_id
        ]

        offset = section_offsets.get(
            section_id,
            0
        )

        y = 180 + offset

        section_offsets[
            section_id
        ] = offset + 140

        positions[
            node["id"]
        ] = {
            "x": x,
            "y": y
        }

    return positions


def build_fan_in_layout(
    data: dict
):

    positions = {}

    center_x = 850
    center_y = 360

    source_y = 180

    for node in data["nodes"]:

        if node["workflow_lane"] == "Signal Sources":

            positions[
                node["id"]
            ] = {
                "x": 120,
                "y": source_y
            }

            source_y += 180

    for node in data["nodes"]:

        if node["workflow_lane"] == "Correlation":

            positions[
                node["id"]
            ] = {
                "x": center_x,
                "y": center_y
            }

        if node["workflow_lane"] == "Dependency Analysis":

            positions[
                node["id"]
            ] = {
                "x": 1250,
                "y": 360
            }

        if node["workflow_lane"] == "Operational Insight":

            positions[
                node["id"]
            ] = {
                "x": 1550,
                "y": 360
            }

    return positions


def build_distributed_layout(
    data: dict
):

    positions = {}

    for node in data["nodes"]:

        lane = node["workflow_lane"]

        if lane == "Failure Domain":

            positions[
                node["id"]
            ] = {
                "x": 120,
                "y": 360
            }

        elif lane == "Coordination":

            positions[
                node["id"]
            ] = {
                "x": 700,
                "y": 360
            }

        elif lane == "Failover":

            positions[
                node["id"]
            ] = {
                "x": 1250,
                "y": 220
            }

        elif lane == "Validation":

            positions[
                node["id"]
            ] = {
                "x": 1550,
                "y": 360
            }

    return positions
