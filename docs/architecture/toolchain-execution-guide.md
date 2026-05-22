# Toolchain Execution Guide

## Purpose

This document explains how to operate the repository toolchain.

The toolchain supports metadata-driven scenario generation, bulk scenario production, topology rendering, governance validation, dependency-aware orchestration, runtime observability, and artifact lineage tracking.

## 1. Bootstrap Runtime

Initializes tool virtual environments and installs dependencies.

Command:

    python .\tools\bootstrap-runtime\main.py

## 2. Manifest Discovery

Validates registered tools and runtime metadata.

Command:

    python .\tools\shared-runtime\manifest-discovery\main.py

## 3. Orchestration Runtime

Runs the toolchain using manifest discovery and dependency governance.

Command:

    python .\tools\orchestration-runtime\main.py

Runtime output:

    tools/runtime-workspace\<run-id>\

Expected files:

    run-context.json
    run-summary.json
    artifacts.json
    artifact-lineage.json
    execution-graph.json
    execution-graph.svg
    logs\

## 4. Bulk Scenario Metadata Generation

Command:

    python .\tools\generators\bulk-scenario-generator\main.py

Input:

    governance\scenario-taxonomy-catalog.csv

Output:

    tools\generators\bulk-scenario-generator\outputs\

## 5. Bulk Scenario Package Generation

Command:

    python .\tools\generators\bulk-scenario-generator\bulk_generate.py

Output:

    scenarios\<lifecycle-level>\<scenario-name>\

## 6. Runtime Registry Export

Command:

    python .\tools\orchestration-runtime\export_registry.py

Output:

    tools\runtime-registry.json

## 7. Runtime Cleanup

Command:

    python .\tools\maintenance\runtime-cleaner\main.py

Policy:

    governance\runtime-cleanup-governance.yaml

## 8. Authoritative Sources

Governance:

    governance\

Shared contracts:

    shared-runtime\

## Recommended Smoke Test

Run:

    python .\tools\bootstrap-runtime\main.py
    python .\tools\shared-runtime\manifest-discovery\main.py
    python .\tools\orchestration-runtime\main.py
    python .\tools\orchestration-runtime\export_registry.py

Expected result:

    bootstrap success
    manifest discovery success
    orchestration success
    runtime registry export success

---

# Artifact Contract Governance

The toolchain uses artifact contracts to define required outputs between runtime stages.

Authoritative contract file:

    /tools/orchestration-runtime/configs/artifact-contracts.yaml

## Contract Purpose

Artifact contracts define:

- required runtime outputs
- downstream execution prerequisites
- validation report dependencies
- governance report dependencies
- visualization artifact requirements

## Current Enforcement Mode

Current mode:

    documentation-aligned governance

Future mode:

    runtime-enforced artifact validation

## Required Artifact Flow

    normalized_metadata
    → relationship_graph
    → scenario_package
    → svg_sources / png_artifacts
    → taxonomy_report
    → relationship_validation_report
    → governance_report

## Governance Rule

governance-checker must not be considered complete unless taxonomy validation and relationship validation outputs are both available.
