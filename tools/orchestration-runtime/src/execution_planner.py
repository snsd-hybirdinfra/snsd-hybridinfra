from src.dependency_resolver import (
    resolve_execution_order
)

from src.dependency_loader import (
    load_dependencies
)


EXECUTION_STATES = {

    "PENDING": "PENDING",
    "READY": "READY",
    "BLOCKED": "BLOCKED",
    "COMPLETED": "COMPLETED",
    "FAILED": "FAILED"
}


def build_execution_plan():

    dependencies = load_dependencies()

    order = resolve_execution_order()

    plan = []

    for tool in order:

        depends_on = []

        if tool in dependencies:

            depends_on = dependencies[
                tool
            ].get(
                "depends_on",
                []
            )

        state = (
            EXECUTION_STATES["READY"]
            if not depends_on
            else EXECUTION_STATES["PENDING"]
        )

        plan.append(
            {
                "tool": tool,
                "depends_on": depends_on,
                "state": state
            }
        )

    return plan


if __name__ == "__main__":

    execution_plan = build_execution_plan()

    print(
        "\nExecution Plan:\n"
    )

    for item in execution_plan:

        print(
            f"{item['tool']} "
            f"[{item['state']}]"
        )

        if item["depends_on"]:

            print(
                f"  depends_on: "
                f"{', '.join(item['depends_on'])}"
            )
