from dataclasses import asdict


def export_metadata(
    metadata
):

    exported = asdict(
        metadata
    )

    exported = {
        key: value
        for key, value
        in exported.items()
        if value is not None
    }

    return exported
