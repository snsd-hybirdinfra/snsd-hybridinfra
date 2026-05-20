from pathlib import Path
from datetime import datetime
import json
import uuid


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

WORKSPACE_ROOT = (
    REPO_ROOT
    / "tools"
    / "runtime-workspace"
)


def create_run_context(
    execution_mode: str = "sequential"
):

    run_id = str(
        uuid.uuid4()
    )

    started_at = (
        datetime.utcnow()
        .isoformat()
        + "Z"
    )

    run_path = (
        WORKSPACE_ROOT
        / run_id
    )

    run_path.mkdir(
        parents=True,
        exist_ok=True
    )

    context = {
        "run_id": run_id,
        "started_at": started_at,
        "execution_mode": execution_mode,
        "workspace": str(run_path)
    }

    context_path = (
        run_path
        / "run-context.json"
    )

    with open(
        context_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context,
            file,
            indent=2
        )

    return context


def create_tool_workspace(
    run_context: dict,
    tool_name: str
):

    tool_workspace = (
        Path(run_context["workspace"])
        / tool_name
    )

    tool_workspace.mkdir(
        parents=True,
        exist_ok=True
    )

    return tool_workspace
