# OpenStack Compute Visibility Module

## Module Purpose

Validates compute service, hypervisor visibility, host state, and workload placement boundaries.

## Lab Boundary

This is a lab-local implementation module for:

labs/05-kolla-openstack-lab/

## Inputs

- Kolla-Ansible configuration state
- OpenStack service container state
- OpenStack API endpoint state
- Service catalog output
- Compute service output
- Network service output
- Recovery workflow results
- Validation output

## Outputs

- Raw OpenStack operational evidence
- Processed service health summaries
- Control plane readiness summaries
- Compute visibility summaries
- Network validation summaries
- Recovery validation summaries
- Scenario evidence summaries
- Lab validation report inputs

## Related Lab Runtime

- shared-runtime/runners/
- shared-runtime/validators/
- shared-runtime/parsers/

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |
