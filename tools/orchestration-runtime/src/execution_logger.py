from datetime import datetime
import json
import time
from pathlib import Path


def utc_now():

    return (
        datetime.utcnow()
        .isoformat()
        + "Z"
    )


def start_tool_log(
    run_context: dict,
    tool_name: str
):

    return {
        "run_id": run_context["run_id"],
        "tool_name": tool_name,
        "status": "running",
        "started_at": utc_now(),
        "ended_at": None,
        "duration_seconds": None,
        "workspace": str(
            Path(run_context["workspace"])
            / tool_name
        ),
        "_start_time": time.time()
    }


def finish_tool_log(
    tool_log: dict,
    status: str,
    error: str = None
):

    ended_at = utc_now()
    duration = (
        time.time()
        - tool_log["_start_time"]
    )

    tool_log["status"] = status
    tool_log["ended_at"] = ended_at
    tool_log["duration_seconds"] = round(
        duration,
        3
    )

    if error:
        tool_log["error"] = error

    tool_log.pop(
        "_start_time",
        None
    )

    return tool_log


def write_tool_log(
    run_context: dict,
    tool_log: dict
):

    log_dir = (
        Path(run_context["workspace"])
        / "logs"
    )

    log_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    log_path = (
        log_dir
        / f"{tool_log['tool_name']}.json"
    )

    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            tool_log,
            file,
            indent=2
        )

    return log_path
