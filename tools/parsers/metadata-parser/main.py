from src.loader import load_yaml
from src.validator import validate_metadata
from src.parser import parse_scenario_metadata
from src.exporter import export_metadata


SCHEMA_PATH = "schemas/scenario-schema.yaml"
EXAMPLE_PATH = "examples/vpn-connectivity-monitoring.yaml"


def main():

    raw_data = load_yaml(EXAMPLE_PATH)

    validate_metadata(
        raw_data,
        SCHEMA_PATH
    )

    metadata = parse_scenario_metadata(raw_data)

    exported = export_metadata(metadata)

    print(exported)


if __name__ == "__main__":
    main()
