from datetime import datetime
from pathlib import Path
import json
import uuid


def utc_now():

    return (
        datetime.utcnow()
        .isoformat()
        + "Z"
    )


def lineage_path(
    run_context: dict
):

    return (
        Path(run_context["workspace"])
        / "artifact-lineage.json"
    )


def load_lineage(
    run_context: dict
):

    path = lineage_path(
        run_context
    )

    if not path.exists():

        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def write_lineage(
    run_context: dict,
    lineage: list
):

    path = lineage_path(
        run_context
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            lineage,
            file,
            indent=2
        )

    return path


def register_artifact_handoff(
    run_context: dict,
    artifact_id: str,
    source_tool: str,
    target_tool: str,
    handoff_type: str
):

    lineage = load_lineage(
        run_context
    )

    handoff = {
        "handoff_id": str(uuid.uuid4()),
        "run_id": run_context["run_id"],
        "artifact_id": artifact_id,
        "source_tool": source_tool,
        "target_tool": target_tool,
        "handoff_type": handoff_type,
        "handed_off_at": utc_now()
    }

    lineage.append(
        handoff
    )

    write_lineage(
        run_context,
        lineage
    )

    return handoff
