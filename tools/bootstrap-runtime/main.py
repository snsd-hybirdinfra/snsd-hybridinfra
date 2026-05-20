from pathlib import Path
import subprocess
import yaml


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


def discover_bootstrap_tools():

    tools = []

    for manifest_path in TOOLS_ROOT.rglob("manifest.yaml"):

        manifest = load_yaml(
            manifest_path
        )

        tool = manifest["tool"]

        if not tool.get("bootstrap", False):

            continue

        if tool.get("state") != "active":

            continue

        tools.append({

            "name":
                tool["name"],

            "path":
                manifest_path.parent,

            "requirements":
                tool.get("requirements"),

            "runtime":
                tool["runtime"],

            "order":
                tool["order"]
        })

    return sorted(
        tools,
        key=lambda item: item["order"]
    )


def bootstrap_tool(tool: dict):

    tool_path = tool["path"]

    venv_path = (
        tool_path
        / "venv"
    )

    python_path = (
        venv_path
        / "Scripts"
        / "python.exe"
    )

    print(
        f"Bootstrapping: {tool['name']}"
    )

    if tool["runtime"] != "python":

        print(
            f"Skipped unsupported runtime: "
            f"{tool['runtime']}"
        )

        return

    if not venv_path.exists():

        subprocess.run(
            [
                "python",
                "-m",
                "venv",
                str(venv_path)
            ],
            check=True
        )

    requirements = tool.get(
        "requirements"
    )

    if requirements:

        requirements_path = (
            tool_path
            / requirements
        )

        if requirements_path.exists():

            subprocess.run(
                [
                    str(python_path),
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    str(requirements_path)
                ],
                check=True
            )

    if tool["name"] == "diagram-renderer":

        subprocess.run(
            [
                str(python_path),
                "-m",
                "playwright",
                "install",
                "chromium"
            ],
            check=True
        )

    print(
        f"{tool['name']} ready."
    )


def main():

    tools = discover_bootstrap_tools()

    print(
        f"Discovered bootstrap tools: "
        f"{len(tools)}"
    )

    for tool in tools:

        bootstrap_tool(
            tool
        )

    print(
        "Manifest-based bootstrap completed."
    )


if __name__ == "__main__":
    main()
