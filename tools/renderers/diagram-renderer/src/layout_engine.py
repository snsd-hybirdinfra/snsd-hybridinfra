NODE_WIDTH = 220
NODE_HEIGHT = 140

LAYER_WIDTH = 300
LAYER_HEIGHT = 300

LEFT_MARGIN = 80
TOP_MARGIN = 150

LAYER_GAP = 360

NODE_X_OFFSET = 40
NODE_Y_OFFSET = 80


def collect_layers(nodes: list):

    layers = []

    for node in nodes:

        if node["layer"] not in layers:

            layers.append(
                node["layer"]
            )

    return layers


def build_layout(topology_nodes: list):

    layers = collect_layers(
        topology_nodes
    )

    node_positions = {}

    layer_positions = {}

    for index, layer in enumerate(layers):

        layer_x = (
            LEFT_MARGIN
            + index * LAYER_GAP
        )

        layer_y = TOP_MARGIN

        layer_positions[layer] = {
            "x": layer_x,
            "y": layer_y,
            "width": LAYER_WIDTH,
            "height": LAYER_HEIGHT
        }

    for node in topology_nodes:

        layer_index = layers.index(
            node["layer"]
        )

        x = (
            LEFT_MARGIN
            + layer_index * LAYER_GAP
            + NODE_X_OFFSET
        )

        y = (
            TOP_MARGIN
            + NODE_Y_OFFSET
        )

        node_positions[node["id"]] = {
            "x": x,
            "y": y,
            "width": NODE_WIDTH,
            "height": NODE_HEIGHT
        }

    canvas_width = (
        LEFT_MARGIN * 2
        + len(layers) * LAYER_GAP
        + 120
    )

    canvas_height = 900

    return {
        "layers": layers,
        "layer_positions": layer_positions,
        "node_positions": node_positions,
        "canvas_width": canvas_width,
        "canvas_height": canvas_height
    }
