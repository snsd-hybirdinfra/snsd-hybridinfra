# Two-Node Expansion Guide

## Purpose

This guide defines how the Linux Observability Lab expands from single-node remote-key execution to two-node managed target validation.

## Expansion Boundary

The two-node mode validates that the lab can operate against more than one Linux host using the same Ansible workflow.

This validates:

- Multi-host inventory parsing
- SSH key-based access to multiple Linux targets
- Become privilege readiness across multiple targets
- Setup workflow execution across multiple targets
- Validation workflow execution across multiple targets
- Evidence capture from multi-host Ansible output

This does not validate:

- Production-scale inventory
- Dynamic inventory integration
- Centralized telemetry ingestion
- Prometheus scrape configuration
- Grafana dashboard publishing

## Required Target Conditions

Each target VM should provide:

| Requirement | Expected State |
|---|---|
| SSH access | user1 reachable from WSL |
| Python | /usr/bin/python3 available |
| Sudo | user1 can become root |
| SSH key | public key installed in authorized_keys |
| Network | reachable from WSL control node |

## Inventory Model

Use inventory/hosts.two-node.example.ini as the template.

The working inventory remains inventory/hosts.ini.

## Execution Flow

1. Confirm SSH access to each target.
2. Confirm Ansible ping for all targets.
3. Confirm become privilege for all targets.
4. Run setup.sh.
5. Run validate.sh.
6. Review generated local evidence summary.

## Evidence Policy

Generated runtime evidence remains under evidence/generated/ and is intentionally ignored by Git.

Reviewer-facing documentation records the execution boundary and validation approach, not raw local runtime evidence.