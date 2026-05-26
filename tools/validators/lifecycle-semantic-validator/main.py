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

from shared_runtime.src.validator_findings import (
    write_validator_findings
)

from shared_runtime.src.validator_findings import (
    write_validator_findings
)

configure_runtime_encoding()

from src.loader import (
    load_rules,
    discover_readmes
)

from src.validator import (
    validate_readme
)

from src.report import (
    write_report
)


def main():

    rules = load_rules()

    readmes = discover_readmes()

    findings = []

    for readme in readmes:

        findings.extend(
            validate_readme(
                readme,
                rules
            )
        )

    write_report(
        findings
    )

    output_path, status = write_validator_findings(
        "lifecycle-semantic-validator",
        findings
    )

    print(
        f"Validator findings written: {output_path}"
    )

    print(
        f"Validator status: {status}"
    )

    if findings:

        print(
            f"Lifecycle semantic validation completed with warnings: {len(findings)}"
        )

    else:

        print(
            "Lifecycle semantic validation passed."
        )


if __name__ == "__main__":
    main()





