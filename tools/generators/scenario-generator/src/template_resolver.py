from pathlib import Path


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parents[1]
)


LEVEL_TEMPLATE_MAP = {

    "level-1-visibility":
        BASE_DIR
        / "templates"
        / "levels"
        / "level-1-visibility"
        / "readme.md.j2",

    "level-2-correlation":
        BASE_DIR
        / "templates"
        / "levels"
        / "level-2-correlation"
        / "readme.md.j2",

    "level-3-recovery":
        BASE_DIR
        / "templates"
        / "levels"
        / "level-3-recovery"
        / "readme.md.j2",

    "level-4-resilience":
        BASE_DIR
        / "templates"
        / "levels"
        / "level-4-resilience"
        / "readme.md.j2",

    "level-5-continuity":
        BASE_DIR
        / "templates"
        / "levels"
        / "level-5-continuity"
        / "readme.md.j2"
}


def resolve_level_template(
    lifecycle_level: str
):

    if lifecycle_level not in LEVEL_TEMPLATE_MAP:

        raise ValueError(
            f"Unknown lifecycle level: "
            f"{lifecycle_level}"
        )

    return LEVEL_TEMPLATE_MAP[
        lifecycle_level
    ]
