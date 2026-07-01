# Linux Observability Lab Execution Guide

## Purpose

This guide describes how to execute the Linux Observability Lab after target hosts are prepared.

## Prerequisites

- Ansible installed on the management node
- SSH access to Linux target nodes
- inventory/hosts.ini updated with reachable target IP addresses
- inventory/ansible.pem available locally if key-based access is used
- target user has sudo privileges

## Execution Order

1. Review inventory/hosts.ini
2. Review inventory/group_vars/linux_observability_targets.yml
3. Run scripts/preflight.sh
4. Run scripts/setup.sh
5. Run scripts/validate.sh
6. Review evidence/generated/
7. Run scripts/cleanup.sh if needed

## Commands

Run from the lab directory:

- bash scripts/preflight.sh
- bash scripts/setup.sh
- bash scripts/validate.sh
- bash scripts/cleanup.sh

## Evidence Output

Generated evidence is written under:

- evidence/generated/raw/
- evidence/generated/processed/
- evidence/generated/summary/

Runtime logs are written under:

- runtime-workspace/logs/

## Current Execution Status

| Area | Status |
|---|---|
| Inventory Skeleton | prepared |
| Ansible Config | prepared |
| Setup Playbook | prepared |
| Validation Playbook | prepared |
| Cleanup Playbook | prepared |
| Runtime Execution | not yet executed |
| Generated Evidence | not yet produced |


---

## Evidence Parsing

The validation workflow runs:

- scripts/parse_evidence.py

The parser converts raw Ansible validation logs into:

- evidence/generated/processed/linux-observability-processed-summary.md
- evidence/generated/summary/linux-observability-execution-summary.md
