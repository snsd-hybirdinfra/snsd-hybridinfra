# Docker Service Container Adapter

## Adapter Purpose

Reads OpenStack service container state and restart boundaries.

## Lab Boundary

This is a lab-local adapter for:

labs/05-kolla-openstack-lab/

## Integration Role

The adapter provides the integration boundary between OpenStack validation workflows and Kolla-Ansible, OpenStack CLI/API, Docker service containers, telemetry systems, or Python evidence parsing.

## Expected Outputs

- Kolla-Ansible readiness result
- OpenStack service status result
- API endpoint validation result
- Compute service visibility result
- Network service validation result
- Service container state result
- Recovery workflow result
- Evidence input data

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
