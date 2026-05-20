from pathlib import Path
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

DEPENDENCY_PATH = (
    REPO_ROOT
    / "governance"
    / "tool-dependency-governance.yaml"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def load_dependency_graph():

    rules = load_yaml(
        DEPENDENCY_PATH
    )

    return rules[
        "tool_dependencies"
    ]


def resolve_execution_order(
    graph: dict
):

    resolved = []
    visiting = set()
    visited = set()

    def visit(tool_name: str):

        if tool_name in visited:
            return

        if tool_name in visiting:
            raise ValueError(
                f"Circular dependency detected: {tool_name}"
            )

        visiting.add(tool_name)

        for dependency in graph[tool_name].get("depends_on", []):

            if dependency not in graph:
                raise ValueError(
                    f"Unknown dependency: {dependency}"
                )

            visit(dependency)

        visiting.remove(tool_name)
        visited.add(tool_name)
        resolved.append(tool_name)

    for tool_name in graph.keys():
        visit(tool_name)

    return resolved


def resolve_execution_groups(
    graph: dict
):

    remaining = set(graph.keys())
    completed = set()
    groups = []

    while remaining:

        ready = []

        for tool_name in sorted(remaining):

            dependencies = set(
                graph[tool_name].get("depends_on", [])
            )

            if dependencies.issubset(completed):

                ready.append(tool_name)

        if not ready:

            raise ValueError(
                "Circular or unresolved dependency detected."
            )

        groups.append(ready)

        for tool_name in ready:

            remaining.remove(tool_name)
            completed.add(tool_name)

    return groups


def main():

    graph = load_dependency_graph()

    groups = resolve_execution_groups(
        graph
    )

    print("Parallel execution groups:")

    for index, group in enumerate(groups, start=1):

        print(
            f"Group {index}: "
            f"{', '.join(group)}"
        )


if __name__ == "__main__":
    main()
