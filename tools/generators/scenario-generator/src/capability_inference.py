import yaml

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]

CAPABILITY_REGISTRY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "registry"
    / "capabilities"
    / "capability-registry.yaml"
)


def load_capability_registry():

    with open(
        CAPABILITY_REGISTRY_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def infer_modules_and_adapters(
    capability_names: list
):

    registry = load_capability_registry()

    capabilities = registry["capabilities"]

    modules = []
    adapters = []

    for capability_name in capability_names:

        if capability_name not in capabilities:

            raise ValueError(
                f"Unknown capability: {capability_name}"
            )

        capability = capabilities[capability_name]

        modules.extend(
            capability.get("supported_modules", [])
        )

        adapters.extend(
            capability.get("supported_adapters", [])
        )

    return {
        "modules": sorted(set(modules)),
        "adapters": sorted(set(adapters))
    }
