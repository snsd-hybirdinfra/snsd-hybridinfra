from pathlib import Path


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

TOOLS_ROOT = (
    REPO_ROOT
    / "tools"
)


def validate_no_nested_tools():

    violations = []

    ignored_parts = {
        "venv",
        "__pycache__",
        "site-packages"
    }

    for path in TOOLS_ROOT.rglob("tools"):

        if path == TOOLS_ROOT:

            continue

        if any(
            part in ignored_parts
            for part in path.parts
        ):

            continue

        violations.append(path)

    if violations:

        for violation in violations:

            print(
                f"Nested tools violation: "
                f"{violation}"
            )

        raise ValueError(
            "Nested tool directories detected."
        )

def validate_no_runtime_workspace_commit_risk():

    runtime_workspace = (
        TOOLS_ROOT
        / "runtime-workspace"
    )

    if runtime_workspace.exists():

        print(
            "Runtime workspace exists locally. "
            "Ensure it remains gitignored."
        )


def main():

    validate_no_nested_tools()

    validate_no_runtime_workspace_commit_risk()

    print(
        "Tool boundary validation passed."
    )


if __name__ == "__main__":
    main()
