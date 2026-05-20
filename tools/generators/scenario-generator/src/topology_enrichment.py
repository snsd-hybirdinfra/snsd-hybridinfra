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


def enrich_topology_nodes(
    topology: dict,
    capabilities: list
):

    registry = load_capability_registry()

    capability_registry = (
        registry["capabilities"]
    )

    for node in topology["nodes"]:

        node["capabilities"] = []

        for capability_name in capabilities:

            if capability_name not in capability_registry:

                continue

            capability = (
                capability_registry[capability_name]
            )

            supported_layers = (
                capability.get(
                    "supported_layers",
                    []
                )
            )

            if node["layer"] in supported_layers:

                node["capabilities"].append(
                    capability_name
                )

    return topology
