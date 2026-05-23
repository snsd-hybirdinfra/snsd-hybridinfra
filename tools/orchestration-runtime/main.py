from pathlib import Path
import os
import subprocess
import yaml

from src.execution_planner import (
    build_execution_plan
)

from src.run_context import (
    create_run_context,
    create_tool_workspace
)

from src.execution_logger import (
    start_tool_log,
    finish_tool_log,
    write_tool_log
)

from src.run_summary import (
    write_run_summary
)

from src.artifact_manifest import (
    register_artifact
)

from src.artifact_lineage import (
    register_artifact_handoff
)

from src.execution_graph import (
    build_execution_graph
)

from src.execution_graph_renderer import (
    render_execution_graph
)

from src.execution_report_writer import (
    write_execution_report
)


REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = REPO_ROOT / "tools"


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def discover_tools():

    tools = {}

    for manifest_path in TOOLS_ROOT.rglob("manifest.yaml"):

        manifest = load_yaml(
            manifest_path
        )

        tool = manifest["tool"]

        if not tool.get("orchestration", False):

            continue

        if tool.get("state") != "active":

            continue

        tools[tool["name"]] = {
            "name": tool["name"],
            "path": manifest_path.parent,
            "entrypoint": tool["entrypoint"],
            "execution_policy": tool.get(
                "execution_policy",
                {}
            )
        }

    return tools


def register_runtime_log_artifact(
    run_context: dict,
    log_path: Path
):

    register_artifact(
        run_context,
        "orchestration-runtime",
        "runtime-log",
        str(log_path)
    )

def execute_tool(
    tool: dict,
    run_context: dict
):

    policy = tool.get(
        "execution_policy",
        {}
    )

    if not policy.get("enabled", True):

        print(
            f"Skipping disabled tool: {tool['name']}"
        )

        return "SKIPPED"

    tool_log = start_tool_log(
        run_context,
        tool["name"]
    )

    tool_path = tool["path"]

    python_path = (
        tool_path
        / "venv"
        / "Scripts"
        / "python.exe"
    )

    main_path = (
        tool_path
        / tool["entrypoint"]
    )

    tool_workspace = create_tool_workspace(
        run_context,
        tool["name"]
    )

    print(
        f"Running: {tool['name']}"
    )

    print(
        f"Workspace: {tool_workspace}"
    )

    if not python_path.exists():

        tool_log = finish_tool_log(
            tool_log,
            "failed",
            f"Missing python executable: {python_path}"
        )

        log_path = write_tool_log(
            run_context,
            tool_log
        )

        register_runtime_log_artifact(
            run_context,
            log_path
        )

        if not policy.get("critical", True):

            print(
                f"Non-critical tool missing python executable: {tool['name']}"
            )

            return "WARNING"

        raise FileNotFoundError(
            f"Python executable not found: {python_path}"
        )

    env = os.environ.copy()

    env["RUN_ID"] = run_context["run_id"]
    env["TOOL_WORKSPACE"] = str(tool_workspace)
    env["EXECUTION_MODE"] = run_context["execution_mode"]

    try:

        result = subprocess.run(
            [
                str(python_path),
                str(main_path)
            ],
            cwd=str(tool_path),
            capture_output=True,
            text=True,
            env=env,
            timeout=300
        )

    except subprocess.TimeoutExpired:

        tool_log = finish_tool_log(
            tool_log,
            "failed",
            "Execution timeout exceeded."
        )

        log_path = write_tool_log(
            run_context,
            tool_log
        )

        register_runtime_log_artifact(
            run_context,
            log_path
        )

        if not policy.get(
            "critical",
            True
        ):

            print(
                f"Non-critical tool timeout: "
                f"{tool['name']}"
            )

            return "WARNING"

        raise RuntimeError(
            f"{tool['name']} timeout exceeded."
        )

    print(result.stdout)

    warning_detected = (
        "WARNING:"
        in result.stdout
    )

    if result.returncode != 0:

        print(result.stderr)

        tool_log = finish_tool_log(
            tool_log,
            "failed",
            result.stderr
        )

        log_path = write_tool_log(
            run_context,
            tool_log
        )

        register_runtime_log_artifact(
            run_context,
            log_path
        )

        if not policy.get("critical", True):

            print(
                f"Non-critical tool failed: {tool['name']}"
            )

            return "WARNING"

        raise RuntimeError(
            f"{tool['name']} execution failed."
        )

    final_status = (
        "WARNING"
        if warning_detected
        else "COMPLETED"
    )

    tool_log = finish_tool_log(
        tool_log,
        final_status.lower()
    )

    log_path = write_tool_log(
        run_context,
        tool_log
    )

    register_runtime_log_artifact(
        run_context,
        log_path
    )

    print(
        f"{tool['name']} {final_status.lower()}."
    )

    return final_status

def finalize_run(
    run_context: dict
):

    summary_path = write_run_summary(
        run_context
    )

    summary_artifact = register_artifact(
        run_context,
        "orchestration-runtime",
        "run-summary",
        str(summary_path)
    )

    register_artifact_handoff(
        run_context,
        summary_artifact["artifact_id"],
        "orchestration-runtime",
        "scenario-governance-validator",
        "governance-input"
    )

    graph_path = build_execution_graph(
        run_context
    )

    register_artifact(
        run_context,
        "orchestration-runtime",
        "execution-graph",
        str(graph_path)
    )

    svg_path = render_execution_graph(
        run_context
    )

    register_artifact(
        run_context,
        "orchestration-runtime",
        "diagram",
        str(svg_path)
    )

    print(
        f"Run summary written: {summary_path}"
    )

    print(
        f"Execution graph written: {graph_path}"
    )

    print(
        f"Execution graph SVG written: {svg_path}"
    )


def main():

    execution_results = []
    execution_status = {}

    run_context = create_run_context()

    print(
        f"Run ID: {run_context['run_id']}"
    )

    tools = discover_tools()

    execution_plan = build_execution_plan()

    print(
        "Dependency-aware orchestration plan:"
    )

    for item in execution_plan:

        tool_name = item["tool"]

        if tool_name not in tools:

            continue

        print(
            f"- {tool_name}"
        )

    for item in execution_plan:

        tool_name = item["tool"]

        depends_on = item.get(
            "depends_on",
            []
        )

        critical = item.get(
            "critical",
            True
        )

        if tool_name not in tools:

            continue

        blocked_dependencies = [
            dependency
            for dependency in depends_on
            if execution_status.get(
                dependency
            ) in [
                "FAILED",
                "BLOCKED"
            ]
        ]

        if blocked_dependencies:

            execution_status[tool_name] = "BLOCKED"

            execution_results.append(
                {
                    "tool": tool_name,
                    "status": "BLOCKED",
                    "notes": (
                        "blocked by failed dependencies: "
                        + ", ".join(blocked_dependencies)
                    )
                }
            )

            print(
                f"Blocked: {tool_name}"
            )

            continue

        try:

            status = execute_tool(
                tools[tool_name],
                run_context
            )

            execution_status[tool_name] = status

            notes = (
                "execution completed with warnings"
                if status == "WARNING"
                else "execution completed"
            )

            execution_results.append(
                {
                    "tool": tool_name,
                    "status": status,
                    "notes": notes
                }
            )

        except Exception as error:

            status = (
                "FAILED"
                if critical
                else "WARNING"
            )

            execution_status[tool_name] = status

            execution_results.append(
                {
                    "tool": tool_name,
                    "status": status,
                    "notes": str(error)
                }
            )

            print(
                f"Execution {status.lower()}: {tool_name}"
            )

            print(
                str(error)
            )

    finalize_run(
        run_context
    )

    write_execution_report(
        execution_results
    )

    print(
        "Runtime-governed orchestration completed."
    )

    
if __name__ == "__main__":
    main()
