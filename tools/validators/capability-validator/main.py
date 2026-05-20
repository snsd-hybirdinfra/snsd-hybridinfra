from pathlib import Path
import yaml


REPO_ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

ALIGNMENT_RULE_PATH = (
    REPO_ROOT
    / "governance"
    / "capabilities"
    / "lifecycle-capability-alignment.yaml"
)

CAPABILITY_REGISTRY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "registry"
    / "capabilities"
    / "capability-registry.yaml"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def resolve_capability_category(
    capability_name: str,
    registry: dict
):

    capabilities = registry.get(
        "capabilities",
        {}
    )

    if capability_name not in capabilities:

        raise ValueError(
            f"Unknown capability: "
            f"{capability_name}"
        )

    return capabilities[
        capability_name
    ]["category"]


def validate_alignment(
    lifecycle_level: str,
    capabilities: list,
    rules: dict,
    registry: dict
):

    lifecycle_rules = (
        rules[
            "lifecycle_capability_alignment"
        ][lifecycle_level]
    )

    allowed = set(
        lifecycle_rules[
            "allowed_categories"
        ]
    )

    blocked = set(
        lifecycle_rules[
            "blocked_categories"
        ]
    )

    warnings = set(
        lifecycle_rules[
            "warning_categories"
        ]
    )

    for capability in capabilities:

        category = (
            resolve_capability_category(
                capability,
                registry
            )
        )

        if category in blocked:

            raise ValueError(
                f"Blocked capability category "
                f"'{category}' "
                f"for lifecycle "
                f"'{lifecycle_level}'"
            )

        if category in warnings:

            print(
                f"WARNING: capability "
                f"'{capability}' uses "
                f"warning category "
                f"'{category}'"
            )

        if category not in allowed \
           and category not in warnings:

            raise ValueError(
                f"Capability category "
                f"'{category}' "
                f"not permitted for "
                f"'{lifecycle_level}'"
            )

    print(
        "Capability alignment validation passed."
    )


def main():

    rules = load_yaml(
        ALIGNMENT_RULE_PATH
    )

    registry = load_yaml(
        CAPABILITY_REGISTRY_PATH
    )

    test_level = "level-3-recovery"

    test_capabilities = [

        "recovery-orchestration",
        "rollback-validation"
    ]

    validate_alignment(
        test_level,
        test_capabilities,
        rules,
        registry
    )


if __name__ == "__main__":
    main()
