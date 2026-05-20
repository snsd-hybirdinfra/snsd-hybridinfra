import yaml

from pathlib import Path
from jsonschema import validate


REPO_ROOT = Path(__file__).resolve().parents[3]


SCHEMA_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "schemas"
    / "topology"
    / "topology-contract.schema.yaml"
)

TOPOLOGY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "schemas"
    / "topology"
    / "examples"
    / "vpn-connectivity-topology.yaml"
)

NODE_REGISTRY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "registry"
    / "nodes"
    / "node-types.yaml"
)

EDGE_REGISTRY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "registry"
    / "edges"
    / "edge-types.yaml"
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


def validate_node_layers(
    topology: dict,
    registry: dict
):

    node_types = registry["node_types"]

    for node in topology["nodes"]:

        node_type = node["type"]
        node_layer = node["layer"]

        if node_type not in node_types:

            raise ValueError(
                f"Unknown node type: {node_type}"
            )

        allowed_layers = (
            node_types[node_type]["allowed_layers"]
        )

        if node_layer not in allowed_layers:

            raise ValueError(
                f"Invalid layer "
                f"'{node_layer}' "
                f"for node type "
                f"'{node_type}'"
            )


def validate_edge_registry(
    topology: dict,
    registry: dict
):

    relationship_types = (
        registry["relationship_types"]
    )

    for edge in topology["edges"]:

        relationship = edge["relationship"]
        direction = edge["direction"]
        criticality = edge["criticality"]

        if relationship not in relationship_types:

            raise ValueError(
                f"Unknown relationship type: "
                f"{relationship}"
            )

        relationship_policy = (
            relationship_types[relationship]
        )

        if direction not in (
            relationship_policy[
                "allowed_directions"
            ]
        ):

            raise ValueError(
                f"Invalid direction "
                f"'{direction}' "
                f"for relationship "
                f"'{relationship}'"
            )

        if criticality not in (
            relationship_policy[
                "allowed_criticality"
            ]
        ):

            raise ValueError(
                f"Invalid criticality "
                f"'{criticality}' "
                f"for relationship "
                f"'{relationship}'"
            )


def validate_capabilities(
    topology: dict,
    registry: dict
):

    capabilities = registry["capabilities"]

    for node in topology["nodes"]:

        node_capabilities = (
            node.get(
                "capabilities",
                []
            )
        )

        for capability_name in node_capabilities:

            if capability_name not in capabilities:

                raise ValueError(
                    f"Unknown capability: "
                    f"{capability_name}"
                )

            capability = (
                capabilities[capability_name]
            )

            supported_layers = (
                capability.get(
                    "supported_layers",
                    []
                )
            )

            if node["layer"] not in supported_layers:

                raise ValueError(
                    f"Capability "
                    f"'{capability_name}' "
                    f"not allowed on layer "
                    f"'{node['layer']}'"
                )


def main():

    schema = load_yaml(
        SCHEMA_PATH
    )

    topology = load_yaml(
        TOPOLOGY_PATH
    )

    node_registry = load_yaml(
        NODE_REGISTRY_PATH
    )

    edge_registry = load_yaml(
        EDGE_REGISTRY_PATH
    )

    capability_registry = load_yaml(
        CAPABILITY_REGISTRY_PATH
    )

    validate(
        instance=topology,
        schema=schema
    )

    validate_node_layers(
        topology,
        node_registry
    )

    validate_edge_registry(
        topology,
        edge_registry
    )

    validate_capabilities(
        topology,
        capability_registry
    )

    print(
        "Topology validation passed."
    )

    print(
        "Node registry validation passed."
    )

    print(
        "Edge registry validation passed."
    )

    print(
        "Capability validation passed."
    )


if __name__ == "__main__":
    main()
