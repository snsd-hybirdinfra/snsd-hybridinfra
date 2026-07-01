# Ansible Automation Lab Shared Runtime

This shared runtime provides lab-local execution helpers for Ansible automation validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute setup, validation, rollback, recovery, and cleanup workflows |
| validators/ | Check inventory, SSH access, playbook results, rollback state, and recovery outcomes |
| parsers/ | Convert Ansible output and command results into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/03-ansible-automation-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
