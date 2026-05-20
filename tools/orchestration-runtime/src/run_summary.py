from pathlib import Path
import json


def load_json(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def write_run_summary(
    run_context: dict
):

    run_path = Path(
        run_context["workspace"]
    )

    log_dir = (
        run_path
        / "logs"
    )

    summary_path = (
        run_path
        / "run-summary.json"
    )

    logs = []

    if log_dir.exists():

        for log_path in sorted(
            log_dir.glob("*.json")
        ):

            logs.append(
                load_json(log_path)
            )

    success_count = len([
        log for log in logs
        if log.get("status") == "success"
    ])

    failed_count = len([
        log for log in logs
        if log.get("status") == "failed"
    ])

    total_duration = sum([
        log.get("duration_seconds", 0)
        for log in logs
    ])

    summary = {
        "run_id": run_context["run_id"],
        "started_at": run_context["started_at"],
        "execution_mode": run_context["execution_mode"],
        "tool_count": len(logs),
        "success_count": success_count,
        "failed_count": failed_count,
        "status": "failed" if failed_count > 0 else "success",
        "duration_seconds": round(total_duration, 3),
        "tools": logs
    }

    with open(
        summary_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=2
        )

    return summary_path
