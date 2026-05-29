REQUIRED_TOP_LEVEL_FIELDS = [
    "diagram",
    "layout",
    "sections",
    "nodes",
    "edges"
]


def validate_schema(
    data: dict
):

    missing = []

    for field in REQUIRED_TOP_LEVEL_FIELDS:

        if field not in data:

            missing.append(
                field
            )

    if missing:

        raise ValueError(
            f"Missing required fields: {missing}"
        )

    return True
