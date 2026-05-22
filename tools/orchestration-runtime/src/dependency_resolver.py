from collections import defaultdict, deque

from src.dependency_loader import (
    load_dependencies
)


def resolve_execution_order():

    dependencies = load_dependencies()

    graph = defaultdict(list)
    indegree = defaultdict(int)

    all_tools = set()

    for tool, config in dependencies.items():

        all_tools.add(tool)

        depends_on = config.get(
            "depends_on",
            []
        )

        for dependency in depends_on:

            all_tools.add(dependency)

            graph[dependency].append(tool)

            indegree[tool] += 1

    for tool in all_tools:

        indegree[tool] = indegree[tool]

    queue = deque([
        tool
        for tool in sorted(all_tools)
        if indegree[tool] == 0
    ])

    result = []

    while queue:

        current = queue.popleft()

        result.append(current)

        for neighbor in graph[current]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:

                queue.append(neighbor)

    if len(result) != len(all_tools):

        raise RuntimeError(
            "Dependency cycle detected."
        )

    return result


if __name__ == "__main__":

    order = resolve_execution_order()

    print(
        "\nExecution Order:\n"
    )

    for step, tool in enumerate(
        order,
        start=1
    ):

        print(
            f"{step}. {tool}"
        )
