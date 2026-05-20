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


def artifact_manifest_path(
    run_context: dict
):

    return (
        Path(run_context["workspace"])
        / "artifacts.json"
    )


def load_artifacts(
    run_context: dict
):

    path = artifact_manifest_path(
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


def write_artifacts(
    run_context: dict,
    artifacts: list
):

    path = artifact_manifest_path(
        run_context
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            artifacts,
            file,
            indent=2
        )

    return path


def register_artifact(
    run_context: dict,
    produced_by: str,
    artifact_type: str,
    artifact_path: str
):

    artifacts = load_artifacts(
        run_context
    )

    artifact = {
        "artifact_id": str(uuid.uuid4()),
        "run_id": run_context["run_id"],
        "produced_by": produced_by,
        "artifact_type": artifact_type,
        "artifact_path": artifact_path,
        "produced_at": utc_now()
    }

    artifacts.append(
        artifact
    )

    write_artifacts(
        run_context,
        artifacts
    )

    return artifact
