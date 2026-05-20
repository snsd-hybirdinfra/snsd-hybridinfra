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

RUNTIME_REGISTRY_PATH = (
    REPO_ROOT
    / "tools"
    / "runtime-registry.json"
)


def load_yaml(path: Path):

    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_dependencies(rules: dict):

    dependencies = rules["tool_dependencies"]

    for tool_name, rule in dependencies.items():

        for dependency in rule.get("depends_on", []):

            if dependency not in dependencies:

                raise ValueError(
                    f"Unknown dependency '{dependency}' "
                    f"declared by '{tool_name}'"
                )

    print("Tool dependency validation passed.")


def main():

    rules = load_yaml(DEPENDENCY_PATH)

    validate_dependencies(rules)


if __name__ == "__main__":
    main()
