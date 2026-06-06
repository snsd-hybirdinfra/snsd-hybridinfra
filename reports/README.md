# Reports

This directory contains repository-level validation, generation, and governance reports for the SNSD Hybrid Infrastructure portfolio.

Reports are used to verify repository consistency, scenario artifact completeness, relationship metadata quality, and generated documentation status.

---

## Report Inventory

| Report | Purpose |
|---|---|
| [Repository Quality Check](./repository-quality-check.md) | Validates required scenario artifacts, poster outputs, missing files, and known bad phrase patterns. |
| [Related Scenarios Generation Report](./related-scenarios-generation-report.md) | Summarizes strict related scenario generation based on exact `primary_domain` matching. |

---

## Current Validation Scope

Repository validation currently covers:

- scenario directory count
- metadata file count
- operational poster SVG/PNG count
- required evidence artifact presence
- small or broken poster PNG detection
- deprecated generic workflow phrase detection
- README related scenario notice validation

---

## Governance Role

Reports support repository-level governance by providing reviewer-readable evidence that generated artifacts and scenario relationships remain consistent across the portfolio.

---

## Summary

The reports layer provides repository-wide operational quality visibility and supports repeatable validation of the portfolio structure.
