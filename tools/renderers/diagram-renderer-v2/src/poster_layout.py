def build_l1_visibility_layout(
    poster: dict
):

    width = poster.get(
        "width",
        2600
    )

    height = poster.get(
        "height",
        1500
    )

    return {
        "canvas": {
            "width": width,
            "height": height
        },

        "header": {
            "x": 60,
            "y": 40,
            "width": width - 120,
            "height": 130
        },

        "main": {
            "x": 60,
            "y": 200,
            "width": 1880,
            "height": 920
        },

        "workflow": {
            "x": 1990,
            "y": 200,
            "width": 550,
            "height": 760
        },

        "dashboard": {
            "x": 60,
            "y": 1235,
            "width": 1880,
            "height": 320
        },

        "summary": {
            "x": 1990,
            "y": 990,
            "width": 550,
            "height": 300
        },

        "legend": {
            "x": 1990,
            "y": 1320,
            "width": 550,
            "height": 235
        },

        "sections": {
            "observed-domain": {
                "x": 80,
                "y": 220,
                "width": 1840,
                "height": 220
            },

            "telemetry-platform": {
                "x": 80,
                "y": 465,
                "width": 1840,
                "height": 220
            },

            "visibility-output": {
                "x": 80,
                "y": 710,
                "width": 1840,
                "height": 220
            },

            "validation-status": {
                "x": 80,
                "y": 955,
                "width": 1840,
                "height": 220
            }
        }
    }


def build_layout(
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

        return build_l1_visibility_layout(
            data.get(
                "poster",
                {}
            )
        )

    return build_l1_visibility_layout(
        data.get(
            "poster",
            {}
        )
    )









