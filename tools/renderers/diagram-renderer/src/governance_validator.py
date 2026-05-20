def validate_required_diagrams(
    lifecycle_level: str,
    diagrams: list,
    governance: dict
):

    required = governance[
        lifecycle_level
    ][
        "required"
    ]

    missing = []

    for diagram in required:

        if diagram not in diagrams:
            missing.append(diagram)

    if missing:

        raise ValueError(
            f"Missing required diagrams: {missing}"
        )

    return True
