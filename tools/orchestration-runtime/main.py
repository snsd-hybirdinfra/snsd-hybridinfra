from pathlib import Path
import subprocess
import yaml
import os

from src.dependency_resolver import (
    load_dependency_graph,
    resolve_execution_order
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

REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

TOOLS_ROOT = (
    REPO_ROOT
    / "tools"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def discover_tools():

    tools = {}

    for manifest_path in TOOLS_ROOT.rglob(
        "manifest.yaml"
    ):

        manifest = load_yaml(
            manifest_path
        )

        tool = manifest["tool"]

        if not tool.get(
            "orchestration",
            False
        ):

            continue

        if tool.get("state") != "active":

            continue

        tools[tool["name"]] = {

            "name":
                tool["name"],

            "path":
                manifest_path.parent,

            "entrypoint":
                tool["entrypoint"]
        }

    return tools


def execute_tool(
    tool: dict,
    run_context: dict
):

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

    tool_workspace = (
        create_tool_workspace(
            run_context,
            tool["name"]
        )
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
            f"Missing python executable: "
            f"{python_path}"
        )

        log_path = write_tool_log(
            run_context,
            tool_log
        )

        register_artifact(
             run_context,
            "orchestration-runtime",
            "runtime-log",
            str(log_path)
        )

        raise FileNotFoundError(
            f"Python executable not found: "
            f"{python_path}"
        )

    env = os.environ.copy()

    env["RUN_ID"] = (
        run_context["run_id"]
    )

    env["TOOL_WORKSPACE"] = (
        str(tool_workspace)
    )

    env["EXECUTION_MODE"] = (
        run_context["execution_mode"]
    )

    result = subprocess.run(
        [
            str(python_path),
            str(main_path)
        ],
        cwd=str(tool_path),
        capture_output=True,
        text=True,
        env=env
    )

    print(result.stdout)

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

        register_artifact(
            run_context,
            "orchestration-runtime",
            "runtime-log",
            str(log_path)
        )

        raise RuntimeError(
        f"{tool['name']} execution failed."
        )

    tool_log = finish_tool_log(
        tool_log,
        "success"
    )

    log_path = write_tool_log(
    run_context,
    tool_log
)

    register_artifact(
    run_context,
    "orchestration-runtime",
    "runtime-log",
    str(log_path)
)

    print(
        f"{tool['name']} completed."
    )


def main():

    run_context = create_run_context()

    print(
        f"Run ID: "
        f"{run_context['run_id']}"
    )

    tools = discover_tools()

    dependency_graph = (
        load_dependency_graph()
    )

    execution_order = (
        resolve_execution_order(
            dependency_graph
        )
    )

    print(
        "Dependency-aware orchestration order:"
    )

    for tool_name in execution_order:

        if tool_name not in tools:

            continue

        print(
            f"- {tool_name}"
        )

    for tool_name in execution_order:

        if tool_name not in tools:

            continue

        execute_tool(
            tools[tool_name],
            run_context
        )
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
    print(
    f"Run summary written: {summary_path}"
    )
    print(
        "Runtime-governed orchestration completed."
    )
    graph_path = build_execution_graph(
        run_context
    )
    svg_path = render_execution_graph(
    run_context
    )

    svg_artifact = register_artifact(
    run_context,
    "orchestration-runtime",
    "diagram",
    str(svg_path)
    )

    print(
    f"Execution graph SVG written: "
    f"{svg_path}"
    )
    graph_artifact = register_artifact(
    run_context,
    "orchestration-runtime",
    "execution-graph",
    str(graph_path)
    )

    print(
        f"Execution graph written: {graph_path}"
    )

if __name__ == "__main__":
    main()
