import yaml
import json

from pathlib import Path
import sys

sys.path.append(
    str(
        Path(__file__).resolve().parents[3]
        / "tools"
    )
)

from shared_runtime.src.runtime_encoding import (
    configure_runtime_encoding
)

configure_runtime_encoding()


REPO_ROOT = Path(__file__).resolve().parents[3]


TOPOLOGY_PATH = (
    REPO_ROOT
    / "shared-runtime"
    / "schemas"
    / "topology"
    / "examples"
    / "vpn-connectivity-topology.yaml"
)

OUTPUT_PATH = (
    REPO_ROOT
    / "tools"
    / "mappers"
    / "relationship-mapper"
    / "outputs"
    / "relationship-graph.json"
)


def load_yaml(path: Path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


def build_relationship_graph(
    topology: dict
):

    graph = {

        "topology_name":
            topology["topology_name"],

        "nodes":
            topology["nodes"],

        "relationships":
            []
    }

    for edge in topology["edges"]:

        graph["relationships"].append({

            "source":
                edge["source"],

            "target":
                edge["target"],

            "relationship":
                edge["relationship"],

            "criticality":
                edge["criticality"]
        })

    return graph


def main():

    topology = load_yaml(
        TOPOLOGY_PATH
    )

    graph = build_relationship_graph(
        topology
    )

    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            graph,
            file,
            indent=2
        )

    print(
        "Relationship graph exported."
    )

    print(
        f"Output: {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()

