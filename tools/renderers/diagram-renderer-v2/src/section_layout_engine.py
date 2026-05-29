def build_section_layout(
    data: dict,
    profile: dict
):

    direction = profile[
        "direction"
    ]

    if direction == "fan-in":

        return build_fan_in_sections()

    if direction == "distributed":

        return build_distributed_sections()

    return build_linear_sections(
        data
    )


def build_linear_sections(
    data: dict
):

    sections = {}

    x = 80

    for section in data["sections"]:

        sections[
            section["id"]
        ] = {
            "x": x,
            "y": 100,
            "width": 300,
            "height": 760
        }

        x += 340

    return sections


def build_fan_in_sections():

    return {
        "signal-sources": {
            "x": 40,
            "y": 140,
            "width": 340,
            "height": 620
        },

        "analysis-layer": {
            "x": 720,
            "y": 260,
            "width": 340,
            "height": 260
        },

        "dependency-layer": {
            "x": 1180,
            "y": 260,
            "width": 320,
            "height": 260
        },

        "operational-insight": {
            "x": 1540,
            "y": 260,
            "width": 260,
            "height": 260
        }
    }


def build_distributed_sections():

    return {
        "regional-failure-domain": {
            "x": 40,
            "y": 260,
            "width": 340,
            "height": 260
        },

        "coordination-layer": {
            "x": 620,
            "y": 260,
            "width": 340,
            "height": 260
        },

        "failover-layer": {
            "x": 1120,
            "y": 140,
            "width": 420,
            "height": 520
        },

        "survivability-layer": {
            "x": 1600,
            "y": 260,
            "width": 260,
            "height": 260
        }
    }
