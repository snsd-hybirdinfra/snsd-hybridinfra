# Kolla OpenStack Lab Shared Runtime

This shared runtime provides lab-local execution helpers for OpenStack operational validation.

## Runtime Areas

| Area | Purpose |
|---|---|
| runners/ | Execute Kolla-Ansible, OpenStack validation, service recovery, telemetry, evidence, and cleanup workflows |
| validators/ | Check service containers, OpenStack APIs, endpoints, compute state, network state, and evidence outputs |
| parsers/ | Convert OpenStack CLI/API output, Docker service state, Kolla output, and validation results into evidence summaries |

## Runtime Boundary

This runtime belongs only to:

labs/05-kolla-openstack-lab/

Repository-level shared-runtime remains a catalog layer.

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
